import json
import tkinter as tk
from tkinter import messagebox
import requests
from constants import USERS_PATH, API_KEY


class EntryWithBuffer(tk.Entry):
    def __init__(self, master=None, is_protected=True, buffer_size=10, **kwargs):
        super().__init__(master, **kwargs)

        self.buffer = [''] * buffer_size
        self.buffer_size = buffer_size
        self.is_protected = is_protected

        self.bind('<KeyRelease>', self.update_buffer)

    def update_buffer(self, event) -> None:
        current = self.get()

        # the "buffer overflow" attack
        if self.is_protected and len(current) > self.buffer_size:
            self.delete(self.buffer_size, tk.END)
            self.update_buffer(event)
            return

        current = list(current)
        self.buffer = [''] * self.buffer_size
        for i in range(len(current)):
            self.buffer[i] = current[i]

    def get_string(self) -> str:
        return ''.join(self.buffer)


def load_users() -> dict:
    try:
        with open(USERS_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def authenticate(username: str, password: str) -> dict:
    users = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]
    else:
        return None


def login(username_entry: EntryWithBuffer, password_entry: EntryWithBuffer, root: tk.Tk, is_protected: bool) -> None:
    username = username_entry.get_string()
    password = password_entry.get_string()

    user = authenticate(username, password)

    if user:
        # the principle of minimizing privileges
        if is_protected:
            if user['role'] == 'admin':
                open_admin_window(username, root, is_protected)
            else:
                open_user_window(username, root, is_protected)
        else:
            open_admin_window(username, root, is_protected)
            open_user_window(username, root, is_protected)
        root.withdraw()
    else:
        messagebox.showerror('Error', 'Invalid username or password!!!')


def on_closing(root: tk.Tk, is_protected: bool):
    root.destroy()
    start(is_protected)


def open_user_window(username: str, root: tk.Tk, is_protected: bool) -> None:
    user_window = tk.Toplevel(root)
    user_window.title(f'Welcome, {username}!')
    center_window(user_window)

    latitude_label = tk.Label(user_window, text='Latitude:')
    latitude_label.pack()
    latitude_entry = EntryWithBuffer(user_window, is_protected)
    latitude_entry.pack()

    longitude_label = tk.Label(user_window, text='Longitude:')
    longitude_label.pack()
    longitude_entry = EntryWithBuffer(user_window, is_protected)
    longitude_entry.pack()

    show_weather_button = tk.Button(user_window, text='Show weather',
                                    command=lambda: show_weather(latitude_entry, longitude_entry, user_window, is_protected))
    show_weather_button.pack()

    user_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, is_protected))


def show_weather(latitude_entry: EntryWithBuffer, longitude_entry: EntryWithBuffer, user_window: tk.Toplevel, is_protected: bool) -> None:
    # DoS attack (denial of service)
    if is_protected:
        show_weather_button = user_window.children['!button']
        show_weather_button.config(state=tk.DISABLED)
        user_window.after(5000, lambda: show_weather_button.config(state=tk.NORMAL))
    
    latitude = latitude_entry.get_string()
    longitude = longitude_entry.get_string()

    # an attack exploiting canonicalization errors
    if is_protected:
        if not is_valid_coordinate(latitude, longitude):
            messagebox.showerror('Error', 'Invalid latitude or longitude!')
            return

    weather_info = get_weather(latitude, longitude)
    display_weather_info(weather_info, user_window)


def is_valid_coordinate(latitude: str, longitude: str) -> bool:
    try:
        latitude = float(latitude)
        longitude = float(longitude)
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            return True
        else:
            return False
    except ValueError:
        return False
    

def get_weather(latitude: str, longitude: str) -> str: 
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp'] 
        temperature_celsius = temperature_kelvin - 273.15 
        city_name = data['name']
        country_name = data['sys'].get('country', 'N/A')
        return f'{city_name}, {country_name}\n{weather_description.capitalize()}, {temperature_celsius:.1f}°C'

    raise Exception('Error while getting weather!!!')


def display_weather_info(weather_info: str, user_window: tk.Toplevel) -> None:
    children = user_window.winfo_children()
    if children:
        last_widget = children[-1]
        if isinstance(last_widget, tk.Label):
            last_widget.destroy()

    weather_label = tk.Label(user_window, text=weather_info)
    weather_label.pack()


def open_admin_window(username: str, root: tk.Tk, is_protected: bool) -> None:
    admin_window = tk.Toplevel(root)
    admin_window.title(f'Welcome, {username}!')
    center_window(admin_window)
    
    new_username_label = tk.Label(admin_window, text='Username:')
    new_username_label.pack()
    new_username_entry = EntryWithBuffer(admin_window, is_protected)
    new_username_entry.pack()

    new_password_label = tk.Label(admin_window, text='Password:')
    new_password_label.pack()
    new_password_entry = EntryWithBuffer(admin_window, is_protected, show='*')
    new_password_entry.pack()

    add_user_button = tk.Button(admin_window, text='Add User', 
                                 command=lambda: add_user(new_username_entry.get_string(), new_password_entry.get_string(), is_protected))
    add_user_button.pack()

    admin_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, is_protected))


def add_user(username: str, password: str, is_protected: bool) -> None:
    users = load_users()

    # an attack exploiting canonicalization errors
    if is_protected:
        if username not in users:
            users[username] = {'password': password, 'role': 'user'}
            with open(USERS_PATH, 'w') as file:
                json.dump(users, file)
            messagebox.showinfo('Success', 'User added successfully!')
        else:
            messagebox.showerror('Error', 'User already exists!')
    else:
        users[username] = {'password': password, 'role': 'user'}
        with open(USERS_PATH, 'w') as file:
            json.dump(users, file)


def center_window(window: tk.Tk) -> None:
    window.geometry('400x200')
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x_offset = (window.winfo_screenwidth() - width) // 2
    y_offset = (window.winfo_screenheight() - height) // 2
    window.geometry(f'+{x_offset}+{y_offset}')
    window.focus_set()


def start(is_protected: bool) -> None:
    root = tk.Tk()
    root.title('Authentication')
    center_window(root)

    username_label = tk.Label(root, text='Username:')
    username_label.pack()
    username_entry = EntryWithBuffer(root, is_protected)
    username_entry.pack()

    password_label = tk.Label(root, text='Password:')
    password_label.pack()
    password_entry = EntryWithBuffer(root, is_protected, show='*')
    password_entry.pack()

    login_button = tk.Button(root, text='Login', 
                             command=lambda: login(username_entry, password_entry, root, is_protected))
    login_button.pack()

    root.mainloop()

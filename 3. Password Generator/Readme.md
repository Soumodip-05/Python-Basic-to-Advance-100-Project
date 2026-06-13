# 🔐 Password Generator

A modern and customizable **Password Generator GUI Application** built using **Python** and **Tkinter** with random password generation, PIN mode, clipboard support, customization controls, and a clean modern interface.

---
# 📸 Application Preview

<p align="center">
  <img src="./images/Random Password.png" width="45%" />
  <img src="./images/Pin Password.png" width="45%" />
</p>

---

# 📌 Project Overview

This project is a desktop-based password generator designed to create:

* Secure random passwords
* Numeric PIN passwords
* Custom-length passwords
* User-controlled password combinations

The application provides a clean modern GUI with instant password generation and clipboard functionality.

---

# ✨ Main Features

## ✅ Modern GUI Interface

* Clean modern layout
* Responsive UI components
* Minimal professional design
* User-friendly controls
* Organized card-style sections

---

## ✅ Random Password Generator

The application can generate highly randomized passwords using:

```python id="9pl4wy"
random.choice()
```

Generated passwords can include:

* Uppercase letters
* Lowercase letters
* Numbers

---

## ✅ PIN Generator Mode

The project includes a dedicated PIN generation system.

### Features

* Numeric-only passwords
* Custom PIN length
* Instant generation

Implemented using:

```python id="8ngg3q"
string.digits
```

---

# 🎛️ Password Customization System

Users can customize passwords using:

* Character length slider
* Letter selection
* Digit selection
* Password mode switching

---

# 🎚️ Slider Control System

The password length is controlled using:

```python id="x26zkm"
tk.Scale()
```

### Features

* Adjustable password size
* Range from 4–50 characters
* Real-time customization

---

# 🧠 Intelligent Password Logic

The application dynamically changes generation logic based on selected mode.

## Random Password Mode

* Uses letters and digits
* Fully customizable

## PIN Mode

* Digits only
* Simplified interface

---

# 🔄 Dynamic Mode Switching

The interface supports:

* Random Password Mode
* PIN Password Mode

Implemented using:

```python id="1z44up"
select_random()
select_pin()
```

The GUI updates automatically when switching modes.

---

# 📋 Clipboard Copy System

Users can instantly copy generated passwords using:

```python id="quw2yi"
clipboard_append()
```

### Features

* One-click copying
* Instant clipboard access
* Success popup notification

---

# ⚠️ Validation & Error Handling

The application safely handles:

* Empty selection states
* Invalid password options
* Missing character categories

Validation system:

```python id="k0n5dl"
messagebox.showwarning()
```

---

# 🎨 GUI System Highlights

## Modern Color Palette

| Purpose              | Color      |
| -------------------- | ---------- |
| Background           | White      |
| Primary Accent       | Blue       |
| Secondary Background | Light Gray |
| Text                 | Dark Gray  |

---

# 🖥️ GUI Components Used

The project uses:

* `Tk()`
* `Frame`
* `Label`
* `Button`
* `Entry`
* `Checkbutton`
* `Scale`
* `StringVar`
* `IntVar`

---

# ⚡ Important Functionalities

## ✅ Automatic Password Generation

The first password is automatically generated when the app starts.

```python id="g0p0pp"
self.generate_password()
```

---

## ✅ Dynamic Interface Control

The options panel automatically hides in PIN mode:

```python id="jlwmif"
self.option_frame.pack_forget()
```

---

## ✅ Real-Time Password Refresh

Users can instantly generate a new password using:

* Refresh button
* Mode switching
* Slider updates

---

# 🏗️ Object-Oriented Programming Structure

The application is fully built using OOP principles.

Main Class:

```python id="j0l1rv"
class PasswordGenerator(tk.Tk)
```

Benefits:

* Better code organization
* Reusable methods
* Easier maintenance
* Scalable architecture

---

# 📂 Project Structure

```bash id="y58ctk"
Password-Generator/
│
├── main.py
├── README.md
└── screenshots/
```

---

# 🚀 Technologies Used

* Python 3
* Tkinter GUI Library
* Random Module
* String Module
* Object-Oriented Programming

---

# 🔐 Password Security Features

The generator supports:

* Randomized characters
* Long password creation
* Numeric PIN generation
* Custom length security

---

# ▶️ How to Run

## 1️⃣ Clone Repository

```bash id="t1e0tr"
git clone https://github.com/Soumodip-05/3. Password Generator.git
```

## 2️⃣ Open Project Folder

```bash id="hjlwmw"
cd 3. Password Generator
```

## 3️⃣ Run Application

```bash id="cvhyf0"
python GUI based password genrator.py
```

---

# 🌟 Future Improvements

Possible future upgrades:

* Symbols support
* Password strength meter
* Dark mode
* Save password feature
* Encrypted vault
* QR code export
* Password history
* Custom themes

---

# 🛡️ Security Notes

This project generates passwords locally on your machine and does not store or upload any data.

---

# 👨‍💻 Author

Developed by **Soumodip Majumdar**

---

# ⭐ Support

If you like this project:

* Star the repository
* Fork the project
* Share feedback
* Contribute improvements

---

# 📜 License

This project is open-source and available under the MIT License.

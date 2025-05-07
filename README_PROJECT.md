# Contact Book Project Overview

## Project Description
This project is a contact book application built using Django, a high-level Python web framework. The application allows users to add, view, edit, and delete contacts. It includes a simple user interface and a RESTful API for managing contacts.

## Tools Used
- **Python**: The primary programming language.
- **Django**: The web framework used for building the application.
- **SQLite**: The database used for storing contact data.
- **HTML/CSS**: For the user interface.
- **JavaScript**: For dynamic client-side functionality (if any).

## Project Structure
- **contact_book/**: The root directory of the Django project.
  - **db.sqlite3**: The SQLite database file.
  - **manage.py**: The command-line utility for administrative tasks.
  - **contact_book/**: The Django project configuration directory.
    - **__init__.py**: Initializes the project as a Python package.
    - **asgi.py**: ASGI configuration for asynchronous support.
    - **settings.py**: Configuration settings for the project.
    - **urls.py**: URL routing configuration.
    - **wsgi.py**: WSGI configuration for web server gateway.
  - **contacts/**: The Django app for managing contacts.
    - **__init__.py**: Initializes the app as a Python package.
    - **admin.py**: Admin site configuration.
    - **apps.py**: App configuration.
    - **forms.py**: Forms for user input.
    - **models.py**: Database models.
    - **tests.py**: Test cases for the app.
    - **urls.py**: URL routing for the app.
    - **views.py**: Views for handling HTTP requests.
    - **migrations/**: Database migration files.
      - **__init__.py**: Initializes the migrations directory.
      - **0001_initial.py**: Initial migration file.
  - **static/**: Static files (CSS, JavaScript, images).
    - **css/**: CSS files.
      - **custom.css**: Custom styles for the application.
  - **templates/**: HTML templates.
    - **contacts/**: Templates for the contacts app.
      - **add_contact.html**: Template for adding a contact.
      - **base.html**: Base template for the application.
      - **contact_list.html**: Template for listing contacts.
      - **delete_contact.html**: Template for deleting a contact.
      - **edit_contact.html**: Template for editing a contact.
  - **scripts/**: Additional scripts.
    - **sync-wiki.ts**: TypeScript script for syncing with a wiki (if applicable).

## Running the Application
1. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

2. **Apply Migrations**:
   ```sh
   python manage.py migrate
   ```

3. **Run the Development Server**:
   ```sh
   python manage.py runserver
   ```

4. **Access the Application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Contributing
Contributions are welcome! Please follow the guidelines in the `CONTRIBUTING.md` file (if available).

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact
For any questions or feedback, please contact [Your Name] at [Your Email].
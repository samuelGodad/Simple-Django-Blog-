# Simple Django Blog

## Description

Simple Django Blog is a web application built using Django, a high-level Python web framework. The project aims to provide a basic blogging platform where users can create, publish, and manage their blog posts.

## Features

- User Registration and Authentication: Users can create an account, log in, and log out to access the blogging functionalities.
- Blog Post Creation and Management: Authenticated users can create new blog posts, edit existing posts, and delete posts.
- Post Categories and Tags: Posts can be categorized into different categories and tagged with relevant keywords for easy organization and search.
- Commenting System: Users can leave comments on blog posts to engage in discussions.
- User Profiles: Each user has a profile page that displays their information and the list of blog posts they have authored.
- Responsive Design: The application is designed to be responsive and user-friendly across different devices and screen sizes.

## Installation
To run the Simple Django Blog locally, follow these steps:
1. Clone the repository:
git clone https://github.com/samuelGodad/Simple-Django-Blog-.git
2. Navigate to the project directory:
cd Simple-Django-Blog-
3. Create a virtual environment:
python3 -m venv env
4. Activate the virtual environment:
. On Windows:
.\env\Scripts\activate
. On macOS and Linux:
source env/bin/activate
5. Install the dependencies:
pip install -r requirements.txt
6. Apply the database migrations:
python manage.py migrate
7. Start the development server:
python manage.py runserver
Access the application in your web browser at http://localhost:8000.
## Contributing
Contributions to Simple Django Blog are welcome! If you find any issues or have any suggestions for improvements, please feel free to open an issue or submit a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for more information.
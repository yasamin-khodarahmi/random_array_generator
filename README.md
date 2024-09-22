# Real-Time Random Array Generator

This project is a web application that generates random arrays using NumPy and sends them to connected clients in real-time using Flask and Flask-SocketIO. The application also stores the generated arrays in a MongoDB database for future reference.

## Features

- Generate random arrays with a minimum size of 10,000 and a range between 0 and 99,999 using NumPy.
- Allow users to specify the size of the array and the range of random numbers.
- Send generated random arrays to all connected clients in real-time using WebSockets.
- Update the front-end display with new arrays as they are generated.
- Store each generated random array in a MongoDB collection.
- Provide an option for users to view previously generated arrays.

## Technologies Used

- Backend: Python, Flask, Flask-SocketIO
- Frontend: HTML, JavaScript, Socket.IO client
- Database: MongoDB
- Data Processing: NumPy

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- MongoDB installed and running
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yasamin-khodarahmi/random_array_generator.git
cd real-time-random-array-generator
```
3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```
5. Make sure MongoDB is running on your system.

## Usage

1. Start the Flask application:
```bash
python app.py
```
3. Open a web browser and navigate to `http://localhost:5000`.

4. Use the interface to generate random arrays:
- Specify the array size (minimum 10,000)
- Set the minimum and maximum values for the random numbers
- Click "Generate Array" to create and display a new array

4. View previously generated arrays using the dropdown menu.

## Project Structure

real-time-random-array-generator/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # Frontend HTML template
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Contact

If you have any questions or feedback, please open an issue on GitHub or contact the maintainer at y.khodarahmi.dev@gmail.com.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [MongoDB](https://www.mongodb.com/)
- [Socket.IO](https://socket.io/)

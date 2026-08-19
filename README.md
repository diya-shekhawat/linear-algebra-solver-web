 🧮 MatrixMate – Linear Algebra Solver

> **Learn • Solve • Visualize**

MatrixMate is an interactive web-based **Linear Algebra Solver** designed to help students understand and solve common linear algebra problems with accurate, step-by-step mathematical solutions.

The application provides a simple and responsive interface where users can enter matrices, select a mathematical operation, and receive detailed solutions.

---

## 🌐 Live Website

🔗 https://linear-algebra-solver-web.onrender.com

---

## ✨ Features

- 🧮 Matrix-based problem solving
- 📋 Easy matrix input
- 📌 Paste matrix values directly into input fields
- 📐 Step-by-step mathematical solutions
- ⚡ Fast calculations using Python and SymPy
- 📱 Responsive design for mobile and desktop
- 🌌 Modern Aurora dark-theme interface
- 🎨 Gradient-based MatrixMate branding
- ⚠️ Input validation and error handling
- 🔄 Clear and Reset functionality

---

## 📚 Supported Operations

### 1. Determinant

Calculate the determinant of matrices with step-by-step explanations.

Currently supports:

- 2 × 2 matrices
- 3 × 3 matrices

---

### 2. Adjoint & Inverse

Calculate:

- Determinant
- Adjoint matrix
- Inverse matrix

The application checks whether the matrix is invertible.

If:

```text
If:
text
det(A) = 0

```

3. Gaussian Elimination

Perform Gaussian elimination step by step, including:

Pivot selection
Row swapping
Pivot normalization
Row elimination
Row echelon form
4. Rank of a Matrix

Calculate the rank of a matrix using row-reduced echelon form.

The solution also shows the number of non-zero rows.

5. Eigenvalues & Eigenvectors

Calculate:

Eigenvalues
Eigenvectors
Trace
Determinant
Characteristic equation
6. Linear Transformation

Apply a transformation matrix to an input vector using:

T(x) = A × x

The resulting vector is displayed with the calculation steps.

🛠️ Technologies Used
Frontend
HTML5
CSS3
JavaScript
Responsive CSS
Google Fonts
Backend
Python
Flask
SymPy
Deployment
GitHub
Render
Gunicorn
📁 Project Structure
linear-algebra-solver-web/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── Script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── solver.py
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/diya-shekhawat/linear-algebra-solver-web.git
2. Open the project directory
cd linear-algebra-solver-web
3. Create a virtual environment

For Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
python app.py

The application will be available at:

http://127.0.0.1:5000
📦 Requirements

The project uses:

Flask
SymPy
Gunicorn

These dependencies are listed in:

requirements.txt
🚀 Deployment

MatrixMate is deployed using Render.

Build Command
pip install -r requirements.txt
Start Command
gunicorn app:app

The application is connected to GitHub and can be automatically redeployed when new changes are pushed.

🧮 How to Use
Step 1

Open MatrixMate.

Step 2

Select the required operation.

For example:

Determinant
Step 3

Select the matrix size.

Step 4

Enter the matrix values.

You can also paste matrix values directly into the matrix input fields.

Example:

1 2 3
4 5 6
7 8 9
Step 5

Click:

Solve
Step 6

View the generated step-by-step solution.

⚠️ Error Handling

MatrixMate includes input validation to prevent incorrect calculations.

The application handles situations such as:

Empty matrix inputs
Empty vector inputs
Invalid matrix values
Non-invertible matrices
Unsupported matrix sizes
Invalid operations

Appropriate error messages are displayed instead of generating misleading results.

📱 Responsive Design

MatrixMate is designed to work across:

💻 Desktop
💻 Laptop
📱 Mobile phones
📟 Tablets

The responsive interface adjusts:

Navigation
Hero section
Buttons
Matrix input fields
Solver cards
Step-by-step results
Topic cards
🎨 Design

MatrixMate uses a modern Aurora-inspired dark interface featuring:

Pink
Purple
Blue
Glassmorphism effects
Gradient buttons
Soft glowing elements
Responsive layouts

The application uses a dark-only visual theme.

🎯 Project Objectives

The main objectives of MatrixMate are:

To simplify linear algebra calculations.
To provide step-by-step mathematical explanations.
To help students understand matrix operations.
To reduce calculation errors.
To provide an interactive learning experience.
To make linear algebra tools accessible on both desktop and mobile devices.
🔮 Future Improvements

Possible future improvements include:

Support for larger matrices
Matrix multiplication
Matrix addition and subtraction
LU decomposition
QR decomposition
Diagonalization
Vector operations
Matrix visualization
More interactive learning content
User accounts
Saved calculations
Additional linear algebra topics
👩‍💻 Developer

Diya Shekhawat

MatrixMate was developed as an interactive Linear Algebra learning and solving project.

📄 License

This project is developed for educational and academic purposes.

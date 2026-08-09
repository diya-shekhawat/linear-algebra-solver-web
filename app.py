from flask import Flask, render_template, request, jsonify
from solver import determinant_solver, inverse_solver, gaussian_solver,rank_solver,eigen_solver,transformation_solver

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():

    data = request.get_json()

    topic = data.get("topic")
    matrix = data.get("matrix")

    # Determinants
    if topic == "determinant":

        result = determinant_solver(matrix)

        return jsonify(result)

    # Adjoint & Inverse
    elif topic == "inverse":

        result = inverse_solver(matrix)

        return jsonify(result)
    elif topic == "gaussian":

         result = gaussian_solver(matrix)

         return jsonify(result)
    elif topic == "rank":

         result = rank_solver(matrix)

         return jsonify(result)
    # Eigenvalues & Eigenvectors
    elif topic == "eigen":

         result = eigen_solver(matrix)

         return jsonify(result)
    elif topic == "transformation":

         vector = data.get("vector")

         result = transformation_solver(matrix, vector)

         return jsonify(result)
    return jsonify({
   
    
        "steps":[

            "This topic is under development."

        ]

    })
    # Gaussian Elimination
    


if __name__ == "__main__":
    app.run(debug=True)


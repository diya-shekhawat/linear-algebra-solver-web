from flask import Flask, render_template, request, jsonify

from solver import (
    determinant_solver,
    inverse_solver,
    gaussian_solver,
    rank_solver,
    eigen_solver,
    transformation_solver
)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():

    try:
        # Check whether request contains JSON
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "error": "No input data received."
            }), 400

        topic = data.get("topic")
        matrix = data.get("matrix")

        # -----------------------------
        # Check topic
        # -----------------------------

        if not topic:
            return jsonify({
                "error": "Please select a topic."
            }), 400

        # -----------------------------
        # Check matrix
        # -----------------------------

        if matrix is None or matrix == []:
            return jsonify({
                "error": "Please enter a matrix before solving."
            }), 400

        # Check for completely empty rows
        if not isinstance(matrix, list) or len(matrix) == 0:
            return jsonify({
                "error": "Please enter a valid matrix."
            }), 400

        for row in matrix:

            if not isinstance(row, list) or len(row) == 0:
                return jsonify({
                    "error": "Please enter all matrix values."
                }), 400

            for value in row:

                if value is None or str(value).strip() == "":
                    return jsonify({
                        "error": "Please fill in all matrix values."
                    }), 400

        # -----------------------------
        # Determinant
        # -----------------------------

        if topic == "determinant":

            result = determinant_solver(matrix)

            return jsonify(result)

        # -----------------------------
        # Inverse
        # -----------------------------

        elif topic == "inverse":

            result = inverse_solver(matrix)

            return jsonify(result)

        # -----------------------------
        # Gaussian Elimination
        # -----------------------------

        elif topic == "gaussian":

            result = gaussian_solver(matrix)

            return jsonify(result)

        # -----------------------------
        # Rank
        # -----------------------------

        elif topic == "rank":

            result = rank_solver(matrix)

            return jsonify(result)

        # -----------------------------
        # Eigenvalues & Eigenvectors
        # -----------------------------

        elif topic == "eigen":

            result = eigen_solver(matrix)

            return jsonify(result)

        # -----------------------------
        # Linear Transformation
        # -----------------------------

        elif topic == "transformation":

            vector = data.get("vector")

            if vector is None or vector == []:
                return jsonify({
                    "error": "Please enter a vector."
                }), 400

            for value in vector:

                if value is None or str(value).strip() == "":
                    return jsonify({
                        "error": "Please fill in all vector values."
                    }), 400

            result = transformation_solver(matrix, vector)

            return jsonify(result)

        # -----------------------------
        # Unknown topic
        # -----------------------------

        else:

            return jsonify({
                "error": "Invalid topic selected."
            }), 400

    # -----------------------------
    # Handle unexpected errors
    # -----------------------------

    except ValueError:
        return jsonify({
            "error": "Please enter valid numerical values."
        }), 400

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "error": "Something went wrong while solving the problem."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)


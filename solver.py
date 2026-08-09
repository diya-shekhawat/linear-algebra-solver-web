SUB = {
    "0":"₀",
    "1":"₁",
    "2":"₂",
    "3":"₃",
    "4":"₄",
    "5":"₅",
    "6":"₆",
    "7":"₇",
    "8":"₈",
    "9":"₉"
}

def subscript(number):
    return "".join(SUB[d] for d in str(number))
def matrix_to_html(matrix):

    rows = matrix.tolist()
    row_count = len(rows)

    html = '<div class="matrix-math">'

    for i, row in enumerate(rows):

        if i == 0:
            left = "⎡"
            right = "⎤"

        elif i == row_count - 1:
            left = "⎣"
            right = "⎦"

        else:
            left = "⎢"
            right = "⎥"

        html += f'<div class="matrix-row-math">'

        html += f'<span class="matrix-bracket">{left}</span>'

        for value in row:

            try:
                value = float(value)

                if value.is_integer():
                    value = int(value)
                else:
                    value = round(value, 3)

            except:
                pass

            html += f'<span class="matrix-value">{value}</span>'

        html += f'<span class="matrix-bracket">{right}</span>'

        html += '</div>'

    html += '</div>'

    return html


def determinant_solver(matrix):

    M = Matrix(matrix)
    rows = len(matrix)

    # ==========================
    # 2 x 2 Determinant
    # ==========================

    if rows == 2:

        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]

        det = (a * d) - (b * c)

        steps = [

            "📌 Step 1 : Given Matrix",

            matrix_to_html(M),

            "📌 Step 2 : Formula",

            "det(A) = ad − bc",

            "📌 Step 3 : Substitute Values",

            f"({a} × {d}) − ({b} × {c})",

            "📌 Step 4 : Calculate",

            f"{a*d} − {b*c}",

            "✅ Final Answer",

            f"det(A) = {det}"

        ]

        return {"steps": steps}

    # ==========================
    # 3 x 3 Determinant
    # ==========================

    elif rows == 3:

        det = M.det()

        a11 = matrix[0][0]
        a12 = matrix[0][1]
        a13 = matrix[0][2]

        m11 = Matrix([
            [matrix[1][1], matrix[1][2]],
            [matrix[2][1], matrix[2][2]]
        ]).det()

        m12 = Matrix([
            [matrix[1][0], matrix[1][2]],
            [matrix[2][0], matrix[2][2]]
        ]).det()

        m13 = Matrix([
            [matrix[1][0], matrix[1][1]],
            [matrix[2][0], matrix[2][1]]
        ]).det()

        steps = [

            "📌 Step 1 : Given Matrix",

            matrix_to_html(M),

            "📌 Step 2 : Expand Along First Row",

            "det(A) = a₁₁C₁₁ − a₁₂C₁₂ + a₁₃C₁₃",

            "📌 Step 3 : Calculate Minors",

            f"M₁₁ = {m11}",

            f"M₁₂ = {m12}",

            f"M₁₃ = {m13}",

            "📌 Step 4 : Substitute",

            f"({a11} × {m11}) − ({a12} × {m12}) + ({a13} × {m13})",

            "✅ Final Answer",

            f"det(A) = {det}"

        ]

        return {"steps": steps}

    else:

        return {
            "steps": [
                "Only 2×2 and 3×3 matrices are supported."
            ]
        }


def inverse_solver(matrix):

    M = Matrix(matrix)

    # Check if the matrix is invertible
    if M.det() == 0:

        return {

            "steps":[

                "Step 1 : Given Matrix",

                matrix_to_html(Matrix(matrix)),

                "Step 2 : Determinant",

                f"det(A) = {M.det()}",

                "Final Answer",

                "Inverse does not exist because determinant = 0."

            ]

        }


    determinant = M.det()

    adjoint = M.adjugate()

    inverse = M.inv()

    steps=[

    "📌 Step 1 : Given Matrix",

    matrix_to_html(Matrix(matrix)),

    "📌 Step 2 : Determinant",

    f"det(A) = {determinant}",

    "📌 Step 3 : Adjoint Matrix",

    matrix_to_html(adjoint),

    "📌 Step 4 : Formula",

    "A⁻¹ = (1 / det(A)) × adj(A)",

    "📌 Step 5 : Substitute Values",

    f"(1/{determinant}) ×\n\n{matrix_to_html(adjoint)}",

    "✅ Final Answer",

    matrix_to_html(inverse.evalf(3))   
    ]

    return {

        "steps":steps

    } 
from copy import deepcopy


def gaussian_solver(matrix):

    A = deepcopy(matrix)

    rows = len(A)
    cols = len(A[0])

    steps = []

    # Step 1
    steps.append("📌 Step 1 : Given Matrix")
    steps.append(matrix_to_html(Matrix(A)))

    r = 0

    for c in range(cols):

        if r >= rows:
            break

        # Find pivot
        pivot = r

        while pivot < rows and A[pivot][c] == 0:
            pivot += 1

        if pivot == rows:
            continue

        # Swap rows
        if pivot != r:

            A[r], A[pivot] = A[pivot], A[r]

            steps.append(f"📌 Swap Row {r+1} ↔ Row {pivot+1}")
            steps.append(matrix_to_html(Matrix(A)))

        pivot_value = A[r][c]

        # Make pivot = 1
        if pivot_value != 1:

            A[r] = [x / pivot_value for x in A[r]]

            pivot_display = round(pivot_value, 3)

            if float(pivot_display).is_integer():
              pivot_display = int(pivot_display)

            steps.append(
                f"📌 R{subscript(r+1)} ← R{subscript(r+1)} ÷ {pivot_display}"
)
            steps.append(matrix_to_html(Matrix(A)))

        # Eliminate below

        for i in range(r + 1, rows):

            factor = A[i][c]

            if factor != 0:

                A[i] = [

                    A[i][j] - factor * A[r][j]

                    for j in range(cols)

                ]

                factor_display = round(factor, 3)

                if float(factor_display).is_integer():
                    factor_display = int(factor_display)

                steps.append(
                    f"📌 R{subscript(i+1)} ← R{subscript(i+1)} − {factor_display} × R{subscript(r+1)}"
)

                

                steps.append(matrix_to_html(Matrix(A)))

        r += 1

    steps.append("✅ Row Echelon Form")
    steps.append(matrix_to_html(Matrix(A)))

    return {

        "steps": steps

    } 
from sympy import Matrix

def rank_solver(matrix):

    M = Matrix(matrix)

    rank = M.rank()

    echelon, pivots = M.rref()

    steps = []

    # Step 1
    steps.append("📌 Step 1 : Given Matrix")
    steps.append(matrix_to_html(M))

    # Step 2
    steps.append("📌 Step 2 : Row Echelon Form")
    steps.append(matrix_to_html(echelon))

    # Step 3
    steps.append("📌 Step 3 : Count Non-Zero Rows")

    non_zero_rows = 0

    for row in echelon.tolist():

        if any(value != 0 for value in row):

            non_zero_rows += 1

    steps.append(f"Non-zero rows = {non_zero_rows}")

    # Final Answer
    steps.append("✅ Final Answer")
    steps.append(f"Rank(A) = {rank}")

    return {

        "steps": steps


    }
from sympy import Matrix, Symbol, Eq, latex


def eigen_solver(matrix):

    M = Matrix(matrix)

    eigen_data = M.eigenvects()

    determinant = M.det()

    trace = M.trace()

    steps = []

    # Step 1
    steps.append("📌 Step 1 : Given Matrix")
    steps.append(matrix_to_html(M))

    # Step 2
    steps.append("📌 Step 2 : Characteristic Equation")
    steps.append("det(A − λI) = 0")

    # Step 3
    steps.append("📌 Step 3 : Matrix Properties")
    steps.append(f"Trace(A) = {trace}<br>Determinant(A) = {determinant}")

    # Step 4
    steps.append("📌 Step 4 : Eigenvalues")

    values = []

    for value, multiplicity, vectors in eigen_data:
        values.append(str(value))

    steps.append(", ".join(values))

    # Step 5
    steps.append("📌 Step 5 : Eigenvectors")

    html = ""

    for value, multiplicity, vectors in eigen_data:

        html += f"<b>Eigenvalue λ = {value}</b><br>"

        for v in vectors:

            html += matrix_to_html(v)

        html += "<br>"

    steps.append(html)

    # Final Answer
    steps.append("✅ Final Answer")
    steps.append("Eigenvalues and Eigenvectors calculated successfully.")

    return {

        "steps": steps

    }
from sympy import Matrix

def transformation_solver(matrix, vector):

    A = Matrix(matrix)
    V = Matrix(vector)

    result = A * V

    steps = []

    # Step 1
    steps.append("📌 Step 1 : Transformation Matrix")
    steps.append(matrix_to_html(A))

    # Step 2
    steps.append("📌 Step 2 : Input Vector")
    steps.append(matrix_to_html(V))

    # Step 3
    steps.append("📌 Step 3 : Formula")
    steps.append("T(x) = A × x")

    # Step 4
    steps.append("📌 Step 4 : Multiply Matrix and Vector")
    steps.append(f"{matrix_to_html(A)} × {matrix_to_html(V)}")

    # Final Answer
    steps.append("✅ Final Answer")
    steps.append(matrix_to_html(result))

    return {
        "steps": steps
    }
const matrix = document.getElementById("matrix");
const vector = document.getElementById("vector");
const vectorSection = document.getElementById("vectorSection");
const result = document.getElementById("result");


// =========================
// CREATE MATRIX
// =========================

function createMatrix() {

    matrix.innerHTML = "";

    const size = parseInt(document.getElementById("size").value);

    for (let i = 0; i < size; i++) {

        const row = document.createElement("div");
        row.className = "matrix-row";

        for (let j = 0; j < size; j++) {

            const input = document.createElement("input");

            input.type = "number";
            input.value = "";

            row.appendChild(input);
        }

        matrix.appendChild(row);
    }

    createVector();
}


// =========================
// CREATE VECTOR
// =========================

function createVector() {

    vector.innerHTML = "";

    const size = parseInt(document.getElementById("size").value);

    for (let i = 0; i < size; i++) {

        const input = document.createElement("input");

        input.type = "number";
        input.className = "vector-input";

        vector.appendChild(input);
    }
}


// =========================
// MATRIX SIZE CHANGE
// =========================

document.getElementById("size").addEventListener(
    "change",
    createMatrix
);


// Create initial matrix
createMatrix();


// =========================
// TOPIC CHANGE
// =========================

document.getElementById("topic").addEventListener("change", function () {

    if (this.value === "transformation") {

        vectorSection.style.display = "block";

    } else {

        vectorSection.style.display = "none";
    }
});


// =========================
// PASTE MATRIX
// =========================

document.getElementById("matrix").addEventListener("paste", function (e) {

    e.preventDefault();

    const text = (e.clipboardData || window.clipboardData)
        .getData("text");

    if (!text.trim()) {
        return;
    }

    const rows = text.trim().split(/\r?\n/);

    const inputs = document.querySelectorAll("#matrix input");

    let index = 0;

    rows.forEach(row => {

        const values = row.trim().split(/\s+/);

        values.forEach(value => {

            if (index < inputs.length) {

                inputs[index].value = value;

                index++;
            }
        });
    });
});


// =========================
// CLEAR BUTTON
// =========================

document.getElementById("clearBtn").onclick = () => {

    document.querySelectorAll("#matrix input")
        .forEach(box => box.value = "");

    document.querySelectorAll("#vector input")
        .forEach(box => box.value = "");

    result.innerHTML = `
        <h2>Step-by-Step Solution</h2>
        <p>Waiting for input...</p>
    `;
};


// =========================
// RESET BUTTON
// =========================

document.getElementById("resetBtn").onclick = () => {

    createMatrix();

    result.innerHTML = `
        <h2>Step-by-Step Solution</h2>
        <p>Waiting for input...</p>
    `;
};


// =========================
// ERROR DISPLAY
// =========================

function showError(message) {

    result.innerHTML = `
        <div class="step-card error-card">

            <div class="step-title">
                ⚠️ Error
            </div>

            <div class="step-content">
                ${message}
            </div>

        </div>
    `;

    result.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}


// =========================
// SOLVE BUTTON
// =========================

document.getElementById("solveBtn").onclick = async () => {

    const topic = document.getElementById("topic").value;

    const size = parseInt(
        document.getElementById("size").value
    );


    // -------------------------
    // CHECK TOPIC
    // -------------------------

    if (!topic) {

        showError("Please select a topic first.");

        return;
    }


    // -------------------------
    // READ MATRIX
    // -------------------------

    const rows = document.querySelectorAll(".matrix-row");

    const matrixData = [];

    let matrixIsEmpty = false;
    let matrixIsInvalid = false;


    rows.forEach(row => {

        const values = [];

        row.querySelectorAll("input").forEach(input => {

            const value = input.value.trim();

            // Empty input
            if (value === "") {

                matrixIsEmpty = true;

                values.push(null);

                return;
            }

            const number = Number(value);

            // Invalid number
            if (Number.isNaN(number)) {

                matrixIsInvalid = true;

                values.push(null);

                return;
            }

            values.push(number);
        });

        matrixData.push(values);
    });


    // -------------------------
    // EMPTY MATRIX CHECK
    // -------------------------

    if (matrixIsEmpty) {

        showError(
            "Please fill in all matrix values before solving."
        );

        return;
    }


    // -------------------------
    // INVALID MATRIX CHECK
    // -------------------------

    if (matrixIsInvalid) {

        showError(
            "Please enter valid numerical values only."
        );

        return;
    }


    // =========================
    // READ VECTOR
    // =========================

    const vectorData = [];

    if (topic === "transformation") {

        const vectorInputs =
            document.querySelectorAll("#vector input");

        let vectorIsEmpty = false;
        let vectorIsInvalid = false;


        vectorInputs.forEach(input => {

            const value = input.value.trim();

            if (value === "") {

                vectorIsEmpty = true;

                return;
            }

            const number = Number(value);

            if (Number.isNaN(number)) {

                vectorIsInvalid = true;

                return;
            }

            vectorData.push([number]);
        });


        if (vectorIsEmpty) {

            showError(
                "Please fill in all vector values before solving."
            );

            return;
        }


        if (vectorIsInvalid) {

            showError(
                "Please enter valid numerical values in the vector."
            );

            return;
        }
    }


    // =========================
    // SHOW LOADING
    // =========================

    result.innerHTML = `
        <h2>📋 Step-by-Step Solution</h2>

        <div class="loading">

            <div class="spinner"></div>

            <p>Calculating...</p>

        </div>
    `;


    try {

        // =========================
        // SEND REQUEST
        // =========================

        const response = await fetch("/solve", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                topic: topic,

                matrix: matrixData,

                vector: vectorData
            })
        });


        // =========================
        // READ RESPONSE
        // =========================

        const data = await response.json();


        // =========================
        // BACKEND ERROR
        // =========================

        if (!response.ok || data.error) {

            showError(
                data.error ||
                "Something went wrong while solving."
            );

            return;
        }


        // =========================
        // CHECK RESULT
        // =========================

        if (!data.steps || !Array.isArray(data.steps)) {

            showError(
                "No solution was returned. Please check your input."
            );

            return;
        }


        // =========================
        // DISPLAY RESULT
        // =========================

        let html = `
            <h2>📋 Step-by-Step Solution</h2>
        `;


        data.steps.forEach(step => {

            let content;


            if (
                step.includes("📌") ||
                step.includes("✅")
            ) {

                content = `
                    <div class="step-title">
                        ${step}
                    </div>
                `;

            } else {

                content = `
                    <div class="step-content">
                        ${step}
                    </div>
                `;
            }


            html += `
                <div class="step-card">
                    ${content}
                </div>
            `;
        });


        result.innerHTML = html;


        result.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });


    } catch (error) {

        console.error("Solve Error:", error);


        showError(
            "Unable to connect to the server. Please try again."
        );
    }
};
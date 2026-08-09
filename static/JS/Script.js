const matrix = document.getElementById("matrix");
const vector = document.getElementById("vector");
const vectorSection = document.getElementById("vectorSection");

function createMatrix() {
    matrix.innerHTML = "";

    let size = parseInt(document.getElementById("size").value);

    for (let i = 0; i < size; i++) {

        let row = document.createElement("div");
        row.className = "matrix-row";

        for (let j = 0; j < size; j++) {

            let input = document.createElement("input");

            input.type = "number";
            input.value = "";

            row.appendChild(input);
        }

        matrix.appendChild(row);
    }
    createVector();
}
function createVector() {

    vector.innerHTML = "";

    let size = parseInt(document.getElementById("size").value);

    for (let i = 0; i < size; i++) {

        let input = document.createElement("input");

        input.type = "number";
        input.className = "vector-input";

        vector.appendChild(input);
    }
}
    
document.getElementById("size").addEventListener("change", createMatrix);

createMatrix();
document.getElementById("topic").addEventListener("change", function () {

    if (this.value === "transformation") {

        vectorSection.style.display = "block";

    } else {

        vectorSection.style.display = "none";

    }

});
// =========================
// Paste Matrix
// =========================

document.getElementById("matrix").addEventListener("paste", function (e) {

    e.preventDefault();

    let text = (e.clipboardData || window.clipboardData).getData("text");

    // Split into rows
    let rows = text.trim().split(/\r?\n/);

    let inputs = document.querySelectorAll("#matrix input");

    let index = 0;

    rows.forEach(row => {

        // Split by spaces OR tabs
        let values = row.trim().split(/\s+/);

        values.forEach(value => {

            if (index < inputs.length) {

                inputs[index].value = value;

                index++;

            }

        });

    });

});

document.getElementById("clearBtn").onclick = () => {

    document.querySelectorAll("#matrix input").forEach(box => box.value = "");

};

document.getElementById("resetBtn").onclick = () => {

    createMatrix();

    document.getElementById("result").innerHTML =
        "<h2>Step-by-Step Solution</h2><p>Waiting for input...</p>";

};

document.getElementById("solveBtn").onclick = async () => {

    let topic = document.getElementById("topic").value;

    let size = parseInt(document.getElementById("size").value);

    

    let rows = document.querySelectorAll(".matrix-row");

    let matrixData = [];

    rows.forEach(row => {

        let values = [];

        row.querySelectorAll("input").forEach(input => {

            values.push(Number(input.value));

        });

        matrixData.push(values);

    });
    // Get vector values (only used for Linear Transformation)

let vectorData = [];

document.querySelectorAll("#vector input").forEach(input => {

    vectorData.push([Number(input.value)]);

});

    let response = await fetch("/solve", {

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

    let data = await response.json();

    const result = document.getElementById("result");

// Loading animation
result.innerHTML = `
<h2>Step-by-Step Solution</h2>
<div class="loading">
    <div class="spinner"></div>
    <p>Calculating...</p>
</div>
`;

setTimeout(() => {

    let html = `<h2>📋 Step-by-Step Solution</h2>`;

data.steps.forEach((step, index) => {

    let title = "";

    if(step.includes("📌") || step.includes("✅")){

        title = `
        <div class="step-title">
            ${step}
        </div>
        `;

    }
    else{

        title = `
        <div class="step-content">
            ${step}
        </div>
        `;

    }

    html += `
        <div class="step-card">
            ${title}
        </div>
    `;

});

result.innerHTML = html;

result.scrollIntoView({
    behavior:"smooth"
});

},600);

};
const themeBtn = document.getElementById("themeToggle");

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("light");

    if(document.body.classList.contains("light")){

        themeBtn.innerHTML="☀️";

    }

    else{

        themeBtn.innerHTML="🌙";

    }

});
document.getElementById('pricing-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve input values
    const customerId = document.getElementById('customer').value;
    const productA = document.getElementById('product-a').value;
    const productB = document.getElementById('product-b').value;
    const productC = document.getElementById('product-c').value;
    const productD = document.getElementById('product-d').value;

    // Create a data object to send to the Python backend
    const data = {
        customer: customerId, // Update key to 'customer'
        'product-a': productA,
        'product-b': productB,
        'product-c': productC,
        'product-d': productD
    };

    // Send data to the Python backend using AJAX
    fetch('/calculate_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the Python backend
        updateResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function updateResults(data) {
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = `
        <h2>Order Summary</h2>
        <p>Customer ID: ${data.customerId}</p>
        <p>Quantity of Product A: ${data.productA}</p>
        <p>Base Unit Price of Product A: ${data.unitPrices.A}</p>
        <p>Line Total (EUR) for Product A: ${data.lineTotals.A.toFixed(2)}</p>
        <p>Quantity of Product B: ${data.productB}</p>
        <p>Base Unit Price of Product B: ${data.unitPrices.B}</p>
        <p>Line Total (EUR) for Product B: ${data.lineTotals.B.toFixed(2)}</p>
        <p>Quantity of Product C: ${data.productC}</p>
        <p>Base Unit Price of Product C: ${data.unitPrices.C}</p>
        <p>Line Total (EUR) for Product C: ${data.lineTotals.C.toFixed(2)}</p>
        <p>Quantity of Product D: ${data.productD}</p>
        <p>Base Unit Price of Product D: ${data.unitPrices.D}</p>
        <p>Line Total (EUR) for Product D: ${data.lineTotals.D.toFixed(2)}</p>
        <p>Total Amount (EUR) Before Discounts: ${data.totalBeforeDiscounts.toFixed(2)}</p>
        <p>Total Amount (EUR) After Discounts: ${data.totalAfterDiscounts.toFixed(2)}</p>
        <!-- Display other calculated results here -->
    `;

    // Show results container
    resultsContainer.style.display = 'block';
}
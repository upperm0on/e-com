document.addEventListener("DOMContentLoaded", function () {
    // Select all the item rows
    const itemRows = document.querySelectorAll('.item-row');
    let totalItems = 0;
    let totalPrice = 0;

    itemRows.forEach(row => {
        const quantityCell = row.querySelector('.product_quantity');
        const priceCell = row.querySelector('.product_price');

        const quantity = parseInt(quantityCell.textContent) || 0;
        const price = parseFloat(priceCell.textContent) || 0;

        // Calculate total for this item
        const itemTotal = quantity * price;

        // Update the total price in the table
        const totalCell = row.querySelector('.total-cell');
        totalCell.textContent = itemTotal.toFixed(2);

        // Update overall totals
        totalItems += quantity;
        totalPrice += itemTotal;
    });

    // Update the total items and total price in the footer
    document.querySelector('.total-items').innerText = totalItems;
    document.querySelector('.total-price').innerText = totalPrice.toFixed(2);
    console.log(document.querySelector('.total-items').innerText)
});

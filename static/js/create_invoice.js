document.addEventListener("DOMContentLoaded", function() {
    var add_item_btn = document.getElementById('show_dialogue');
    var search_box = document.querySelector('.search-box');
    var dim_background = document.querySelector('.dim-background');
    var done_btn = document.getElementById('done_button');
    var totalItemsCell = document.querySelector('.total-items');
    var totalPriceCell = document.querySelector('.total-price');

    // Set session storage to false on initial page load if not set
    if (sessionStorage.getItem('showSearchDialogue') === null) {
        sessionStorage.setItem('showSearchDialogue', 'false');
    }

    // Check session storage to decide whether to show search box
    var showSearchDialogue = sessionStorage.getItem('showSearchDialogue');
    if (showSearchDialogue === 'true') {
        search_box.style.display = "block";
        dim_background.style.display = "block";
    }

    add_item_btn.addEventListener('click', function() {
        search_box.style.display = "block";
        dim_background.style.display = "block";
        // Store in session storage that search dialogue should be shown
        sessionStorage.setItem('showSearchDialogue', 'true');
    });

    done_btn.addEventListener('click', function() {
        search_box.style.display = "none";
        dim_background.style.display = "none";
        // Remove from session storage
        sessionStorage.setItem('showSearchDialogue', 'false');
    });

    // JavaScript function to clear items
    window.clearItems = function() {
        if (confirm("Are you sure you want to clear all items?")) {
            var form = document.createElement('form');
            form.method = 'POST';
            form.action = '.';

            var csrf = document.createElement('input');
            csrf.type = 'hidden';
            csrf.name = 'csrfmiddlewaretoken';
            csrf.value = '{{ csrf_token }}';

            var clearButton = document.createElement('input');
            clearButton.type = 'hidden';
            clearButton.name = 'clear_items';

            form.appendChild(csrf);
            form.appendChild(clearButton);

            document.body.appendChild(form);
            form.submit();
        }
    }

    // Function to update the total items and total price
    function updateTotals() {
        var totalItems = 0;
        var totalPrice = 0;
        var quantityInputs = document.querySelectorAll('.quantity-input');

        quantityInputs.forEach(function(input) {
            var row = input.parentNode.parentNode; // Get the parent <tr> of the input
            var price = parseFloat(input.getAttribute('data-price')); // Get the price from data attribute
            var quantity = parseInt(input.value); // Get the quantity from the input
            var itemTotal = price * quantity;

            row.querySelector('.total-cell').textContent = itemTotal.toFixed(2); // Update item total cell

            totalItems += quantity;
            totalPrice += itemTotal;
        });

        totalItemsCell.textContent = totalItems;
        totalPriceCell.textContent = totalPrice.toFixed(2);
    }

    // Add event listener to each quantity input
    var quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(function(input) {
        input.addEventListener('input', updateTotals);
        input.addEventListener('blur', restrictQuantity);
    });

    // Function to restrict quantity to initial value on blur
    function restrictQuantity() {
        var initialQuantity = parseInt(this.getAttribute('value')); // Initial quantity from input value attribute
        var currentQuantity = parseInt(this.value); // Current quantity from input value

        // Ensure quantity is within initial range and not less than zero
        if (isNaN(currentQuantity) || currentQuantity < 0) {
            this.value = initialQuantity; // Reset to initial quantity if less than 0 or NaN
        } else if (currentQuantity > initialQuantity) {
            this.value = initialQuantity; // Reset to initial quantity if more than initial
        }

        // Update totals after restricting quantity
        updateTotals();
    }

    // Initial call to update totals on page load
    updateTotals();
});

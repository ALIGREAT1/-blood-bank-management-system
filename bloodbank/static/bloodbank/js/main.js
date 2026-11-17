
document.addEventListener("DOMContentLoaded", function () {

    // 1. Highlight the active navigation link
    const currentPath = window.location.pathname;

    const navigationLinks = document.querySelectorAll(".nav-link");

    navigationLinks.forEach(function (link) {

        const linkPath = new URL(link.href).pathname;

        if (linkPath === currentPath) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }

    });

    // 2. Automatically dismiss Django messages
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";

            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 4000);

    });

    // 3. Confirm before deleting records
    const deleteButtons = document.querySelectorAll("[data-confirm]");

    deleteButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            const message = button.dataset.confirm;

            if (!confirm(message)) {
                event.preventDefault();
            }

        });

    });

    // 4. Search and filter table records
    const searchInputs = document.querySelectorAll(
        "[data-table-search]"
    );

    searchInputs.forEach(function (input) {

        input.addEventListener("input", function () {

            const targetSelector = input.dataset.tableSearch;
            const table = document.querySelector(targetSelector);

            if (!table) return;

            const searchValue = input.value.toLowerCase();

            const rows = table.querySelectorAll("tbody tr");

            rows.forEach(function (row) {

                const rowText = row.textContent.toLowerCase();

                row.style.display = rowText.includes(searchValue)
                    ? ""
                    : "none";

            });

        });

    });

    // 5. Validate forms before submission
    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function (event) {

            if (!form.checkValidity()) {

                event.preventDefault();
                form.reportValidity();

            }

        });

    });

    // 6. Prevent accidental double submission
    const submitForms = document.querySelectorAll("form");

    submitForms.forEach(function (form) {

        form.addEventListener("submit", function () {

            if (!form.checkValidity()) return;

            const submitButton = form.querySelector(
                'button[type="submit"], input[type="submit"]'
            );

            if (submitButton) {

                submitButton.disabled = true;
                submitButton.textContent = "Processing...";

            }

        });

    });

    console.log("Blood Bank JavaScript loaded successfully.");

});
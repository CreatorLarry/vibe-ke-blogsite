// Custom Admin JavaScript for Vibe-KE Blog

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialize Bootstrap popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Add confirmation for delete actions
    const deleteButtons = document.querySelectorAll('.deletelink');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
    
    // Add confirmation for bulk actions
    const actionSelect = document.querySelector('#changelist-form select[name="action"]');
    if (actionSelect) {
        const form = actionSelect.closest('form');
        form.addEventListener('submit', function(e) {
            const selectedAction = actionSelect.value;
            if (selectedAction && selectedAction !== '') {
                const checkboxes = document.querySelectorAll('#changelist-form input[type="checkbox"]:checked');
                if (checkboxes.length === 0) {
                    e.preventDefault();
                    alert('Please select at least one item to perform this action.');
                    return;
                }
                
                if (selectedAction.includes('delete') || selectedAction.includes('remove')) {
                    if (!confirm(`Are you sure you want to ${selectedAction.replace(/_/g, ' ')} ${checkboxes.length} item(s)?`)) {
                        e.preventDefault();
                    }
                }
            }
        });
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Add hover effect to table rows
    const tableRows = document.querySelectorAll('.table tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#fff3f3';
        });
        
        row.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '';
        });
    });
});
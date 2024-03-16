// Adjust the height of the iframe based on the viewport height minus toolbar height
function adjustIframeHeight() {
    var toolbarHeight = document.querySelector('.toolbar').offsetHeight;
    var iframe = document.querySelector('iframe');
    if (iframe) {
        var windowHeight = window.innerHeight;
        iframe.style.height = (windowHeight - toolbarHeight) + 'px';
    }
}

// Hide sheet tabs
function hideSheetTabs() {
    var iframe = document.getElementById('embeddedSheet');
    var sheetTabsContainer = iframe.contentDocument.querySelector('.docs-sheet-tab-area');
    if (sheetTabsContainer) {
        sheetTabsContainer.style.display = 'none';
    }
}

// Toggle dropdown visibility
function toggleDropdown(dropdownId, show) {
    var dropdownContent = document.getElementById(dropdownId);
    dropdownContent.style.display = show ? 'block' : 'none';
}

// Collapse dropdowns when tapping outside on mobile devices or clicking inside the embedded sheet
function collapseDropdownsOnMobile(event) {
    if (window.innerWidth <= 768 && !event.target.closest('.dropdown')) {
        var dropdownContents = document.querySelectorAll('.dropdown-content');
        dropdownContents.forEach(function(content) {
            content.style.display = 'none';
        });
    }
    if (window.innerWidth <= 768 && event.target.closest('#embeddedSheet')) {
        var dropdownContents = document.querySelectorAll('.dropdown-content');
        dropdownContents.forEach(function(content) {
            content.style.display = 'none';
        });
    }
}

// Handle dropdown click events
function handleDropdownClick(event, dropdownId) {
    var dropdownContent = document.getElementById(dropdownId).querySelector('.dropdown-content');
    toggleDropdown(dropdownContent.id, dropdownContent.style.display === 'none');
    event.stopPropagation();
}

// Add event listeners
window.addEventListener('resize', adjustIframeHeight);
document.getElementById('embeddedSheet').addEventListener('load', function() {
    hideSheetTabs();
    adjustIframeHeight();
});

// IcosSearch JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize application
    initializeSearch();
    initializeVoiceSearch();
    initializeSearchOptions();
    initializeKeyboardShortcuts();
});

function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    const searchForm = document.querySelector('.search-form');
    
    // Focus on search input when page loads
    searchInput.focus();
    
    // Handle form submission
    searchForm.addEventListener('submit', function(e) {
        const query = searchInput.value.trim();
        if (!query) {
            e.preventDefault();
            showMessage('Please enter a search query', 'warning');
        }
    });
    
    // Auto-suggestions (basic implementation)
    searchInput.addEventListener('input', function() {
        // Could implement search suggestions here
        clearMessage();
    });
}

function initializeVoiceSearch() {
    const voiceBtn = document.getElementById('voice-search');
    const searchInput = document.getElementById('search-input');
    
    // Check if browser supports speech recognition
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        voiceBtn.style.display = 'none';
        return;
    }
    
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';
    
    voiceBtn.addEventListener('click', function() {
        if (voiceBtn.classList.contains('voice-active')) {
            recognition.stop();
            return;
        }
        
        voiceBtn.classList.add('voice-active');
        recognition.start();
        showMessage('Listening... Speak now', 'info');
    });
    
    recognition.addEventListener('result', function(event) {
        const transcript = event.results[0][0].transcript;
        searchInput.value = transcript;
        voiceBtn.classList.remove('voice-active');
        clearMessage();
        
        // Auto-submit if transcript is not empty
        if (transcript.trim()) {
            document.querySelector('.search-form').submit();
        }
    });
    
    recognition.addEventListener('error', function(event) {
        voiceBtn.classList.remove('voice-active');
        let errorMessage = 'Voice search error';
        
        switch(event.error) {
            case 'no-speech':
                errorMessage = 'No speech detected. Please try again.';
                break;
            case 'audio-capture':
                errorMessage = 'Microphone not accessible.';
                break;
            case 'not-allowed':
                errorMessage = 'Microphone access denied.';
                break;
            default:
                errorMessage = 'Voice search unavailable.';
        }
        
        showMessage(errorMessage, 'error');
    });
    
    recognition.addEventListener('end', function() {
        voiceBtn.classList.remove('voice-active');
    });
}

function initializeSearchOptions() {
    const optionBtns = document.querySelectorAll('.option-btn');
    
    optionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            optionBtns.forEach(b => b.classList.remove('active'));
            
            // Add active class to clicked button
            this.classList.add('active');
            
            // Get search type
            const searchType = this.getAttribute('data-type');
            
            // Update search form action based on type
            updateSearchType(searchType);
        });
    });
}

function updateSearchType(type) {
    const searchForm = document.querySelector('.search-form');
    const searchInput = document.getElementById('search-input');
    
    // Update placeholder based on search type
    const placeholders = {
        'web': 'Search privately...',
        'images': 'Search for images...',
        'news': 'Search for news...',
        'videos': 'Search for videos...'
    };
    
    searchInput.placeholder = placeholders[type] || placeholders['web'];
    
    // Store search type for form submission
    searchForm.setAttribute('data-search-type', type);
}

function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Focus search input with Ctrl+K or Cmd+K
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            document.getElementById('search-input').focus();
        }
        
        // Voice search with Ctrl+Shift+V
        if (e.ctrlKey && e.shiftKey && e.key === 'V') {
            e.preventDefault();
            document.getElementById('voice-search').click();
        }
    });
}

function showMessage(text, type = 'info') {
    // Remove existing message
    clearMessage();
    
    const message = document.createElement('div');
    message.className = `message message-${type}`;
    message.textContent = text;
    
    // Style the message
    message.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 20px;
        border-radius: 6px;
        color: white;
        font-weight: 500;
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    // Set color based on type
    const colors = {
        'info': '#3498db',
        'warning': '#f39c12',
        'error': '#e74c3c',
        'success': '#27ae60'
    };
    
    message.style.backgroundColor = colors[type] || colors['info'];
    
    document.body.appendChild(message);
    
    // Auto-remove after 3 seconds
    setTimeout(() => {
        clearMessage();
    }, 3000);
}

function clearMessage() {
    const existingMessage = document.querySelector('.message');
    if (existingMessage) {
        existingMessage.remove();
    }
}

// Add CSS animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

// Performance monitoring
function logPerformance() {
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                const perfData = performance.timing;
                const loadTime = perfData.loadEventEnd - perfData.navigationStart;
                console.log(`Page load time: ${loadTime}ms`);
            }, 0);
        });
    }
}

logPerformance();

// Service worker registration (if available)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Could register a service worker for offline functionality
        console.log('Service Worker support detected');
    });
}

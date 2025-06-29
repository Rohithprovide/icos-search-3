# Whoogle Search - Replit Deployment

## Overview

This repository contains a Whoogle Search deployment wrapper for Replit. Whoogle Search is a privacy-focused Google search proxy that removes ads, tracking, and JavaScript while providing clean search results. The application is built with Python/Flask and designed to be easily deployable on various platforms including Replit.

## System Architecture

### Backend Architecture
- **Framework**: Flask web application written in Python
- **Core Components**:
  - Search proxy engine that queries Google and filters results
  - Request handling system with Tor support
  - Configuration management with user preferences
  - Session management with encryption
  - Filter system for cleaning search results
  - Bang shortcuts for quick navigation

### Frontend Architecture
- **Templates**: Jinja2 templating with responsive HTML
- **Styling**: CSS with theme support (light/dark/system)
- **JavaScript**: Vanilla JS for autocomplete, keyboard navigation, and utilities
- **Responsive Design**: Mobile-first approach with separate mobile templates

### Data Flow
1. User submits search query through web interface
2. Flask routes process the request and apply user configurations
3. Search class constructs Google search query with privacy parameters
4. Request module fetches results (optionally through Tor)
5. Filter module processes HTML, removes tracking, ads, and unwanted content
6. Results are rendered with custom templates and returned to user

## Key Components

### Core Modules
- **`app/__init__.py`**: Flask application initialization and configuration
- **`app/routes.py`**: Main route handlers for search, config, and utilities
- **`app/filter.py`**: HTML filtering and result cleaning logic
- **`app/request.py`**: HTTP request handling with Tor support
- **`app/utils/search.py`**: Search query processing and construction

### Models
- **`Config`**: User preference management and session handling
- **`Endpoint`**: URL endpoint enumeration
- **`GClasses`**: Google CSS class tracking for filtering

### Frontend Assets
- **Templates**: HTML templates for search results, configuration, and layouts
- **CSS**: Theming system with variables and responsive design
- **JavaScript**: Client-side functionality for search enhancement

### Configuration System
- Environment variable based configuration
- User session preferences with encryption
- Country, language, and search customization options
- Theme and appearance settings

## External Dependencies

### Python Packages
- **Flask**: Web framework and routing
- **BeautifulSoup4**: HTML parsing and manipulation
- **Requests**: HTTP client for search queries
- **Cryptography**: Session encryption and security
- **Stem**: Tor network integration
- **Waitress**: WSGI server for production deployment

### Optional Integrations
- **Tor Network**: Anonymous search routing
- **Proxy Support**: SOCKS and HTTP proxy compatibility
- **Translation Services**: Multi-language interface support

## Deployment Strategy

### Replit Deployment
- **Entry Point**: `main.py` - Sets up and runs Whoogle Search
- **Process**: 
  1. Clones Whoogle Search repository if not present
  2. Installs Python dependencies
  3. Configures environment for Replit hosting
  4. Starts Flask application server

### Environment Configuration
- Automatic dependency installation from `requirements.txt`
- Environment variable configuration for Replit compatibility
- Port and host configuration for cloud deployment

### Scalability Considerations
- Stateless application design for horizontal scaling
- Session-based user preferences without persistent storage
- Configurable proxy and Tor support for distributed deployment

## Changelog
- June 29, 2025. Initial setup
- June 29, 2025. UI improvements to search results page header:
  - Fixed logo alignment with search bar
  - Increased search bar width from 584px to 700px
  - Removed blue focus border from search bar
  - Improved logo positioning with proper centering
- June 29, 2025. Enhanced autocomplete suggestions to integrate seamlessly with search bar:
  - Modified CSS to make autocomplete suggestions appear as unified element with search bar
  - Updated border-radius to connect search bar and suggestions (24px 24px 0 0 for search bar, 0 0 24px 24px for suggestions)
  - Improved positioning to eliminate gaps between search bar and autocomplete dropdown
  - Enhanced styling across all theme files (header.css, light-theme.css, main.css) for consistency
  - Added proper z-index and positioning for optimal display
- June 29, 2025. Corrected autocomplete to properly match Google's interface:
  - Reverted to dropdown approach with seamless connection to search bar
  - Search bar maintains normal size with suggestions appearing in clean dropdown below
  - Modified border-radius to connect search bar (24px 24px 4px 4px) with dropdown (0 0 24px 24px)
  - Reduced padding and improved spacing to match Google's compact design
  - Positioned dropdown absolutely below search bar with proper z-index and shadows
  - Updated all CSS files for consistent Google-like autocomplete appearance
- June 29, 2025. Fixed autocomplete container visibility issue:
  - Hidden autocomplete container by default (display: none)
  - Only shows when it contains suggestions (:not(:empty) selector)
  - Removed unwanted grey line that appeared below search bar
  - Updated all CSS theme files for consistent behavior
- June 29, 2025. Perfected Google-style autocomplete seamless connection:
  - Search bar rounds only top corners when autocomplete is active (24px 24px 0 0)
  - Autocomplete dropdown rounds only bottom corners (0 0 24px 24px)
  - Removed bottom border from search bar when connected to dropdown
  - Creates unified visual element exactly like Google's interface
  - Applied consistent styling across all theme files
- June 29, 2025. Implemented JavaScript-based dynamic autocomplete styling:
  - Modified autocomplete.js to dynamically change search bar styling
  - Search bar border-radius changes to "24px 24px 0 0" when suggestions appear
  - Automatically resets to normal "24px" styling when suggestions disappear
  - Updated CSS to use specific #autocomplete-list ID targeting
  - Applied changes across all theme files for consistent behavior
- June 29, 2025. Added functional search bar icons with hover effects and voice search:
  - Created voice-search.js with Web Speech API integration
  - Added Google-style hover effects for microphone icon (grey background, scale animation)
  - Implemented voice recognition that fills search bar with spoken text
  - Added visual feedback during recording (red color, pulse animation)
  - Included error handling for microphone permissions and speech recognition
  - Applied consistent hover styling across all theme files (light, dark, header)
  - Microphone icon shows tooltip and handles browser compatibility

## User Preferences

Preferred communication style: Simple, everyday language.
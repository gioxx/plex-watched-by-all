# Watched (Jellyfin – Watched by Everyone)

Web dashboard to explore what’s been watched in Jellyfin. It highlights content completed by all selected users, and exposes full viewing history per user (movies, seasons, and episodes).

## What you’ll see
- **Movies**: Titles marked as watched by every selected user.
- **Seasons (complete)**: Seasons where every episode was watched by every selected user, with total runtime shown.
- **User history**: Full watch history for a chosen user (movies + series). Series cards open a detail page listing the episodes seen, with dates and per-episode posters.
- **Episode detail page**: Per-series breakdown, grouped by season, sorted by most recent viewing.

## Data sources and scope
- Pulls directly from Jellyfin watch history and metadata (posters, ratings, runtime, play count).
- Actually compatible with Jellyfin only.

## Interaction notes
- Use the **Users** selector to choose which Jellyfin users are considered when computing “watched by everyone.”
- **Refresh** triggers a manual cache refresh.
- Search filters within the current tab.
- Missing posters are indicated; items without posters are hidden where appropriate.

## Localization
- UI text is fully localized via JSON locale files (`static/locales/en.json`, `static/locales/it.json`).
- Language is selectable in the header and persists per browser via local storage. Add more locales by dropping a new JSON file and wiring it in `static/index.html` and `static/history_detail.html`.

## Current status
- Frontend-only usage is supported via the shipped HTML/JS/CSS. Deployment/build and container notes will be added later.***

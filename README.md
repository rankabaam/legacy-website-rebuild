# Legacy Website Rebuild

A sanitized WordPress rebuild case study focused on maintainability, information architecture, recurring media operations, and public-facing reliability.

## Portfolio Update: Community Language School and Latest-Message Pattern (October 2026)

Added a **self-contained, responsive Korean language learning landing-page sample** inspired by recent community-page design work, and a **fictional recent-message layout** illustrating the WordPress Query Loop pattern. These are deliberately standalone demonstrations: no production WordPress export, credentials, live forms, or original site theme are published.

- [Responsive language-program sample](samples/community_hangul_program.html)
- [Illustrative recent-message cards](samples/sample_recent_sermons.html)
- [Language-program design notes](docs/hangul_program_case_study.md)
- [Latest-message archive pattern](docs/latest_messages_query_loop.md)

Run the independent tests with `python -m unittest discover -s tests -v`. Download the HTML files to view them in a browser. **This commit does not deploy or modify the live site.**

---

## Overview

This project documents the replacement of an aging legacy CMS with a more maintainable WordPress-based structure. The work included assessing inherited content, rebuilding navigation, reorganizing public media, and connecting the website to recurring workflows such as event updates, sermon publishing, and live-translation access.

The repository is a case study and sample-layout collection rather than a production WordPress export.

## What the Project Demonstrates

- Legacy-site assessment and risk identification
- Information-architecture redesign around visitor tasks
- Migration into a maintainable WordPress structure
- Gallery, sermon, and media archive organization
- Event-calendar refinement for recurring public information
- Integration points for sermon-video and live-translation workflows
- Operational maintenance planning and handoff documentation
- Separation of public design decisions from production infrastructure

## Generalized Project Flow

```text
Legacy-site assessment
        ↓
Content and navigation inventory
        ↓
Information-architecture redesign
        ↓
WordPress rebuild
        ↓
Gallery, event, and media organization
        ↓
Related workflow integration
        ↓
Recurring maintenance and refinement
```

## Documentation

- [Background](docs/background.md)
- [Rebuild Goals](docs/rebuild_goals.md)
- [Rebuild Challenges](docs/rebuild_challenges.md)
- [Information Architecture](docs/information_architecture.md)
- [Media and Gallery Structure](docs/media_and_gallery_structure.md)
- [Translation Integration](docs/translation_integration.md)
- [Maintenance Notes](docs/maintenance_notes.md)
- [Operational Maintenance Model](docs/operational_maintenance.md)
- [Event Calendar Refinement](docs/event_calendar_refinement.md)
- [Media Workflow Integration](docs/media_workflow_integration.md)
- [Lessons Learned](docs/lessons_learned.md)

## Sample Files

- `samples/sample_menu_structure.md`
- `samples/sample_homepage_layout.html`
- `samples/sample_gallery_archive_layout.html`
- `samples/sample_media_archive_layout.html`
- `samples/sample_sermon_video_page.html`

These are simplified demonstrations, not production website files.

## Portfolio Scope

This repository contains no administrator credentials, server configuration, database exports, private records, original media, contact lists, unpublished schedules, backup archives, or security settings.

## Current Status

The repository now documents both the rebuild itself and the recurring operational work required to keep a public website useful after launch.

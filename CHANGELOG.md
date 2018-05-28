# Changelog

## 0.5.1 (Pre-release)

- Fix bug where slug max length was too short for titles.

## 0.5.0 (Pre-release)

- Show pīkau titles on pathway diagram when required. (fixes #49)
- Add 'What is computational thinking?' and 'Computational thinking - The international perspective' pīkau. (fixes #50)
- Update pikau content pages to be closer to iQualify style.
- Fix release script calling invalid command. (fixes #48)
- Update licence. (fixes #52)
- Pīkau documentation updates:
  - Update documentation regarding usage of images and videos. (fixes #53)
  - State box formatting cannot be used within overview. (fixes #43)

## 0.4.4 (Pre-release)

- Update glossary definitions from CS Field Guide material.
- Remove 'Example Pikau' from being loaded (but keep source files as example).
- Dependency updates:
  - Update django-tables2 from 2.0.0a2 to 2.0.0a3.

## 0.4.3 (Pre-release)

- Update pīkau course content rendering to match iQualify.
- Ensure all pīkau models can be modified via admin interface.

## 0.4.2 (Pre-release)

- Display pīkau cover photos with center positioning.
- Alter pīkau content unit header to display course name instead of module name.
- Update "Getting the most out of your time" pīkau:
  - Name changed to "Getting the most out of pīkau".
  - Minor grammar changes.

## 0.4.1 (Pre-release)

- Display pīkau content with iQualify style navigation.
- Add "Getting the most out of your time" pīkau.

## 0.4.0 (Pre-release)

- Add files application for tracking files and their licences. (fixes #34)
  - Display warning if any files have unknown licence. (fixes #36)
  - Allow filtering of files by licence type.
  - Allow users to add and update files.
- Allow users to add and update pīkau glossary entries.
- Begin process of replacing manual HTML tables with tables from django-tables2.
- Dependency updates:
  - Add django-tables2 2.0.0a2.
  - Add django-filter 1.1.0.
  - Update django from 2.0.4 to 2.0.5.
  - Update django-allauth from 0.35.0 to 0.36.0.
  - Update django-anymail from 2.0 to 2.2.
  - Update django-debug-toolbar from 1.8 to 1.9.1.
  - Update psycopg2 from 2.7.3.1 to 2.7.4.
  - Update gunicorn from 19.7.1 to 19.8.1.
  - Update python-markdown-math from 0.3 to 0.5.

## 0.3.0 (Pre-release)

- Add milestone list and detail pages, with table showing milestone statuses. (fixes #9)
- Add basic searching for FAQ page. (fixes #26)
- Improve formatting of pīkau documentation.
- Fix typo in pīkau docs. (fixes #29)
- Change 'Pīkau' to 'pīkau'. (fixes #30)

## 0.2.0 (Pre-release)

- Readiness level is now optional. (fixes #24)
- Add tags to connect pīkau to Self Review Tool (SRT). (fixes #21)
- Explain website and pipeline with documentation. (fixes #14)
- Add link to Google Doc template. (fixes #13)
- Add contact page (further plans to add email form to page).
- Update levels to reflect available options within iQualify.
- Tags now have an optional description.
- Fix bug where readiness level name was duplicated on pathways diagram legend.
- Fix some table sizing issues.

## 0.1.0 (Pre-release)

- Initial release of the KTAM content pipeline assistant.

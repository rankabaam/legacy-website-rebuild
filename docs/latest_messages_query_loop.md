# Latest Messages and Archive Pattern

The rebuild included a WordPress post-based archive and latest-message presentation. This portfolio describes the **design pattern** only.

## Generic WordPress approach

1. Publish an authorized message as a WordPress post.
2. Assign a designated public category and relevant period tag.
3. Use Gutenberg Query Loop blocks to fetch the most recently published matching posts on the landing page.
4. Keep the archive filtered and readable separately, with stable links to public posts.
5. If the publishing automation is unavailable, authorized content editors can continue publishing manually.

The [standalone HTML preview](../samples/sample_recent_sermons.html) is a fictional, static sample. It **does not** implement WordPress API calls, a WordPress theme, or the site's production configuration.

## Non-disclosure

No production WordPress export, site administrator details, category IDs, publishing tokens, post IDs, private media, or plugin configuration is shared.

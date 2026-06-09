# Uploading the social preview image

GitHub's REST/GraphQL API does not currently accept Open Graph image uploads, so this is a one-time manual step.

1. Go to https://github.com/sapuyou45-bit/ai-divination-skills/settings.
2. Scroll to **Social preview**.
3. Click **Edit** → **Upload an image…**.
4. Pick `.github/social-preview-1280x640.png` from this repository.
5. Save.

After upload, the README header card and every shared link (Twitter / X, Slack, LinkedIn, Discord) will show the project preview instead of the default repo grid.

The PNG is sized 1280×640 with 80px safe padding, which is GitHub's recommended ratio. If you ever want to regenerate it, the source is `.github/social-preview.svg`.

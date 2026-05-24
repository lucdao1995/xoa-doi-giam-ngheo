# Prompt Template: Deploy workflow

Khi cần setup CI/CD hoặc xử lý vấn đề deploy:

## Kiến trúc
Source .txt → system3.py → Hugo content (Markdown) → Hugo build → public/ → GitHub Pages → (optional) Cloudflare

## GitHub Actions
File: `hugo-site/.github/workflows/hugo-deploy.yml`
Trigger: push to main
Uses: peaceiris/actions-hugo@v2 + actions/deploy-pages@v4

## Steps if deploy fails
1. Check Actions tab on GitHub — xem log build
2. Test locally: `cd hugo-site && hugo --minify`
3. Common issues: front matter YAML syntax, missing theme files
4. Fix → commit → push again

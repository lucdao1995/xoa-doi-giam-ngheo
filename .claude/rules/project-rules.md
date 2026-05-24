# Project Rules — Xoá Đói Giảm Nghèo

## Skills
Load skill `prompt-master` before generating any prompt.
When asked to "write a prompt for X tool", use prompt-master to generate it.

## Project Structure
- Hugo site: `hugo-site/`
- Raw translation: `xoá đói giảm nghèo - bản dịch hoàn chỉnh.txt`
- Chapter files: `chuong/chuong-*.txt`
- Hugo content: `hugo-site/content/chuong/chuong-*.md`
- Theme: `hugo-site/themes/doc-truyen/`
- Generator: `system3.py` — run this to regenerate Hugo content from source .txt
- Config: `hugo-site/config.toml`

## Workflow
1. Edit source file `.txt` (NOT markdown in content/)
2. Run `python3 system3.py` to regenerate Hugo content
3. Test with `hugo server -D` in `hugo-site/`
4. Commit and push — GitHub Actions auto-deploys

## Style Guide (translation)
- 扶贫 → xóa đói giảm nghèo
- Chu Đình → "hắn" (chủ đạo), "gã"
- Tô Mạn → "cô"
- Chu Viễn → "nó", "thằng nhóc"
- Sentences: 200-400 chars, compound clauses
- Sensory: tactile + olfactory descriptions
- Avoid Hán Việt, use thuần Việt

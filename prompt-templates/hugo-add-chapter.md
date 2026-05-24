# Prompt Template: Thêm chương mới vào Hugo

Khi cần thêm chương mới hoặc sửa nội dung:

## Steps
1. Sửa file gốc: `xoá đói giảm nghèo - bản dịch hoàn chỉnh.txt`
2. Chạy: `python3 system3.py` (tự động sinh lại markdown + metadata)
3. Kiểm tra: `cd hugo-site && hugo server -D`
4. Confirm navigation đúng (prev/next chapter links)
5. Commit + push → GitHub Actions deploy

## File structure
- Source: `xoá đói giảm nghèo - bản dịch hoàn chỉnh.txt` — format `Chương X: Tên`
- Output Hugo content: `hugo-site/content/chuong/chuong-XXX.md`
- Front matter: title, chapter, weight, slug

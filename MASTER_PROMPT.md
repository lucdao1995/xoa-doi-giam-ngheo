# MASTER PROMPT — Dự án Xoá Đói Giảm Nghèo

> Copy-paste prompt này khi làm việc với AI để giữ consistency.

## 📋 Mô tả dự án

Truyện **"Xoá đói giảm nghèo"** (tác giả: Ngụy Ám Thời Khắc) — bản dịch hoàn chỉnh 30 chương.
Thể loại: Ngôn tình, Cấm kỵ, Niên thượng, HE.

Hệ thống xuất bản:
```
Viết truyện (Markdown) → GitHub → Hugo build → GitHub Pages → Cloudflare → Người đọc
```

## 📁 Cấu trúc thư mục

```
truyen-dich/truyen-1/
├── MASTER_PROMPT.md               # File này
├── translation-style-guide.md     # Style guide dịch thuật
├── system3.py                     # Script sinh Hugo content từ file dịch gốc
├── blogger_upload.py              # (cũ) Upload Blogger
├── config.json
├── chapters.json                  # Metadata
├── xoá đói giảm nghèo - bản dịch hoàn chỉnh.txt  # File dịch gốc
├── chuong/                        # Raw text chapters (tách sẵn)
├── html/                          # (cũ) HTML tĩnh
├── blogger/                       # (cũ) Blogger data
└── hugo-site/                     # ★ HUGO SITE CHÍNH
    ├── config.toml                # Hugo config
    ├── .gitignore
    ├── meta.json
    ├── content/
    │   ├── _index.md              # Trang chủ (synopsis)
    │   └── chuong/
    │       ├── chuong-001.md
    │       ├── chuong-002.md
    │       └── ... → chuong-030.md
    ├── themes/doc-truyen/         # Custom theme đọc truyện
    │   ├── layouts/_default/
    │   │   ├── baseof.html        # Layout chính
    │   │   ├── list.html          # Mục lục
    │   │   └── single.html        # Đọc chương
    │   ├── layouts/partials/
    │   │   └── nav.html           # ◀ Mục lục | Chương trước | Chương sau ▶
    │   └── static/css/
    │       └── style.css          # Style
    └── .github/workflows/
        └── hugo-deploy.yml        # CI/CD: push main → build → deploy Pages
```

## 🚀 Workflow

### Khi có bản dịch mới / sửa chữa:
```bash
cd truyen-dich/truyen-1
python3 system3.py          # Sinh lại Markdown từ file dịch gốc
cd hugo-site
hugo server -D              # Xem thử local
# Nếu OK:
git add .
git commit -m "Cập nhật nội dung"
git push                    # GitHub Actions tự build + deploy
```

### Lần đầu setup:
```bash
cd truyen-dich/truyen-1/hugo-site
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
# Settings → Pages → Source: GitHub Actions (nó tự nhận)
```

## 🎨 Theme "doc-truyen" — tính năng

- Mục lục 30 chương (list.html)
- Đọc chương với navigation ◀ ▶ (single.html)
- Responsive (mobile-first)
- Weight-based ordering (không phụ thuộc tên file)
- Hugo partials cho nav (xuất hiện cả đầu và cuối chapter)

## 📝 Style Guide (tóm tắt)

| Từ gốc | Dịch |
|---------|------|
| 扶贫 | xóa đói giảm nghèo |
| 苏老师 | Cô Tô |
| 周霆 | Chu Đình |
| 周远 | Chu Viễn |
| 苏蔓 | Tô Mạn |

- Chu Đình → "hắn" (chủ đạo), "gã", "người đàn ông"
- Tô Mạn → "cô"
- Chu Viễn → "nó", "thằng nhóc"
- Câu dài 200-400 ký tự, ghép nhiều mệnh đề
- Thiên về tactile + olfactory (xúc giác + khứu giác)
- Thuần Việt, tránh Hán Việt khó hiểu

## ⚙️ Config Hugo (config.toml)

```toml
baseURL = "/"
languageCode = "vi-vn"
title = "Xoá đói giảm nghèo"
theme = "doc-truyen"
[params]
  author = "Ngụy Ám Thời Khắc"
  genre = "Ngôn tình, Cấm kỵ, Niên thượng, HE"
  repo = "https://github.com/<user>/<repo>"
[permalinks]
  chuong = "/chuong/:slug/"
```

## 🔗 Cloudflare (sau khi có GitHub Pages)

1. Thêm domain vào Cloudflare
2. Trỏ CNAME → `<user>.github.io`
3. Page Rules: cache everything, SSL Full
4. Worker (optional): redirect `chuong-1` → `chuong/chuong-1/`

## 📌 Lưu ý

- `system3.py` là script chính để sinh content — **không edit markdown thủ công**, sửa file `.txt` gốc rồi chạy lại script
- File `.txt` gốc có 1493 dòng, 30 chương, format `Chương X: Tên chương`
- Navigation dùng `.Params.chapter` (số) thay vì `.PrevInSection` để tránh lỗi ordering
- GitHub Actions dùng `peaceiris/actions-hugo@v2` + `actions/deploy-pages@v4`

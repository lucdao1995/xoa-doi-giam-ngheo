#!/usr/bin/env python3
"""
Hệ thống Hugo - Xoá đói giảm nghèo
Sinh toàn bộ cấu trúc Hugo site từ file dịch.

Cách dùng:
  python3 system3.py
  cd hugo-site && hugo server -D  # Xem thử ở local
"""
import re, os, json, html

SRC = "/home/openclaw/opencode/truyen-dich/truyen-1/xoá đói giảm nghèo - bản dịch hoàn chỉnh.txt"
HUGO_DIR = "/home/openclaw/opencode/truyen-dich/truyen-1/hugo-site"
CONTENT_DIR = os.path.join(HUGO_DIR, "content", "chuong")

STORY_TITLE = "Xoá đói giảm nghèo"
STORY_AUTHOR = "Ngụy Ám Thời Khắc"
STORY_GENRE = "Ngôn tình, Cấm kỵ, Niên thượng, HE"


def parse_chapters():
    """Đọc file gốc, trích xuất 30 chương + synopsis."""
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()

    # Synopsis
    synopsis = ""
    syn_match = re.search(r"Văn án:\s*\n(.*?)(?=\n\n\n+Chương 1:)", text, re.DOTALL)
    if syn_match:
        raw = syn_match.group(1).strip()
        # Collapse paragraphs
        paras = [p.strip() for p in raw.split("\n\n") if p.strip()]
        synopsis = "\n\n".join(paras)

    # Split chapters
    pattern = r"(Chương \d+:[^\n]*)\n"
    parts = re.split(pattern, text)

    chapters = []
    pending_title = None

    for part in parts:
        part = part.strip()
        if not part:
            continue
        if re.match(r"Chương \d+:", part):
            pending_title = part
        elif pending_title:
            m = re.match(r"Chương (\d+):\s*(.*)", pending_title)
            num = int(m.group(1)) if m else len(chapters) + 1
            name = m.group(2).strip() if m else ""
            # Check if we should skip (already captured via title)
            # Chapter 1 is first, so don't skip
            chapters.append({
                "number": num,
                "title": f"Chương {num}: {name}",
                "name": name,
                "content": part,
            })
            pending_title = None

    chapters.sort(key=lambda x: x["number"])

    # Save metadata
    meta = {
        "title": STORY_TITLE,
        "author": STORY_AUTHOR,
        "genre": STORY_GENRE,
        "synopsis": synopsis,
        "total": len(chapters),
        "chapters": chapters,
    }
    with open(os.path.join(HUGO_DIR, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"✓ Parse: {len(chapters)} chương + synopsis")
    return meta


def text_to_markdown(text):
    """Chuyển nội dung chương sang Markdown."""
    paragraphs = []
    for block in text.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        # Multi-line paragraph → join
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        para = " ".join(lines)
        paragraphs.append(para)
    # Return as markdown paragraphs
    return "\n\n".join(paragraphs)


def generate_hugo_content(meta):
    """Sinh file Markdown cho Hugo."""
    os.makedirs(CONTENT_DIR, exist_ok=True)

    for ch in meta["chapters"]:
        num = ch["number"]
        slug = f"chuong-{num}"
        content_md = text_to_markdown(ch["content"])

        # Escape quotes for YAML front matter title
        safe_title = ch["title"].replace('"', "'")

        md = f"""---
title: "{safe_title}"
chapter: {num}
weight: {num}
slug: "{slug}"
---

{content_md}
"""
        filepath = os.path.join(CONTENT_DIR, f"chuong-{num:03d}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)

    print(f"✓ Sinh {len(meta['chapters'])} file Markdown → {CONTENT_DIR}/")


def generate_index_content(meta):
    """Sinh _index.md cho trang chủ."""
    synopsis = meta.get("synopsis", "")
    synopsis_md = text_to_markdown(synopsis)

    md = f"""---
title: "{STORY_TITLE}"
---

{synopsis_md}

---

📖 **{len(meta['chapters'])} chương** · {STORY_AUTHOR} · {STORY_GENRE}
"""
    filepath = os.path.join(HUGO_DIR, "content", "_index.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✓ Sinh _index.md (trang chủ)")


def update_config(meta):
    """Cập nhật config.toml với thông tin mới nhất."""
    config_path = os.path.join(HUGO_DIR, "config.toml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = f.read()

    # Update description
    config = re.sub(
        r'description = ".*"',
        f'description = "Bản dịch hoàn chỉnh · {len(meta["chapters"])} chương"',
        config,
    )

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config)
    print(f"✓ Cập nhật config.toml")


def main():
    print("=" * 60)
    print(f"  {STORY_TITLE} → Hugo Site Generator")
    print("=" * 60)
    print()

    meta = parse_chapters()
    generate_hugo_content(meta)
    generate_index_content(meta)
    update_config(meta)

    print()
    print("=" * 60)
    print("  ✅ HOÀN TẤT")
    print(f"  📁 Hugo site: {HUGO_DIR}/")
    print()
    print("  📖 Để xem thử ở local:")
    print(f"     cd {HUGO_DIR} && hugo server -D")
    print()
    print("  🚀 Để deploy:")
    print("     1. Tạo repo GitHub và push code lên")
    print("     2. Vào Settings → Pages → source = GitHub Actions")
    print("     3. Push lên branch main → tự động build & deploy")
    print()
    print("  ☁️ Cloudflare (tuỳ chọn):")
    print("     Trỏ CNAME tên miền → <user>.github.io")
    print("     Bật proxy Cloudflare (orange cloud)")
    print("=" * 60)


if __name__ == "__main__":
    main()

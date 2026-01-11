#!/usr/bin/env python3
"""Enhance existing blogs in a directory.

This script demonstrates how to use the BlogEnhancer to improve
existing blog posts with better SEO, expanded content, and more.
"""

import time
import warnings
from pathlib import Path

from pencraft import BlogEnhancer, Settings

warnings.filterwarnings("ignore", message="This package.*has been renamed")


def main() -> None:
    """Enhance existing blog posts."""

    # Directory containing blogs to enhance
    # Change this to your blog directory
    blog_dir = Path("./output/high-cpc-2026-blogs")

    # Create settings (uses your existing Pencraft config)
    settings = Settings(
        llm={
            "base_url": "http://localhost:3030/v1",
            "api_key": "dummy-key",
            "temperature": 0.7,
            "max_tokens": 8192,
        },
        blog={
            "min_word_count": 3000,
            "max_word_count": 6000,
        },
    )

    # Progress callback
    def on_progress(msg: str) -> None:
        print(f"   ► {msg}")

    # Create enhancer
    enhancer = BlogEnhancer(settings=settings, on_progress=on_progress)

    print("=" * 70)
    print("🚀 Pencraft: Blog Enhancement Tool")
    print("=" * 70)

    if not blog_dir.exists():
        print(f"❌ Directory not found: {blog_dir}")
        print("Please update the blog_dir variable to point to your blog directory.")
        return

    # Option 1: Enhance a single file
    # Uncomment to use:
    # single_file = blog_dir / "your-blog-post.md"
    # if single_file.exists():
    #     print(f"\n📝 Enhancing single file: {single_file.name}")
    #     result = enhancer.enhance(
    #         single_file,
    #         target_word_count=3000,
    #         improve_seo=True,
    #         use_trends=True,
    #         backup=True,
    #     )
    #     print(f"   ✅ {result.original_word_count} → {result.enhanced_word_count} words")

    # Option 2: Enhance entire directory
    print(f"\n📂 Enhancing directory: {blog_dir}")
    print("=" * 70)

    start_time = time.time()

    results = enhancer.enhance_directory(
        blog_dir,
        pattern="*.md",
        recursive=False,
        skip_on_error=True,
        delay_seconds=2.0,  # Delay between files
        target_word_count=3000,
        improve_seo=True,
        use_trends=True,
        backup=True,
    )

    elapsed = time.time() - start_time

    # Summary
    print("\n" + "=" * 70)
    print("📊 Enhancement Complete!")
    print("=" * 70)

    successful = [r for r in results if not r.error]
    failed = [r for r in results if r.error]

    print(f"   ✅ Successful: {len(successful)}")
    print(f"   ❌ Failed: {len(failed)}")
    print(f"   ⏱  Time: {elapsed:.1f}s")

    if successful:
        total_before = sum(r.original_word_count for r in successful)
        total_after = sum(r.enhanced_word_count for r in successful)
        print(f"   📈 Words: {total_before:,} → {total_after:,} (+{total_after - total_before:,})")

    if failed:
        print("\n❌ Failed files:")
        for r in failed:
            print(f"   • {r.file_path.name}: {r.error}")

    print("=" * 70)


if __name__ == "__main__":
    main()

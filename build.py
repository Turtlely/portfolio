import shutil
from pathlib import Path
import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

POSTS_DIR = Path("posts")
PROJECTS_DIR = Path("projects")
TEMPLATES_DIR = Path("templates")
STATIC_DIR = Path("static")
OUTPUT_DIR = Path("docs")
PHOTOS_DIR = STATIC_DIR / "media" / "photography"
IMAGE_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
DEFAULT_TEMPLATE = "post.html"
RECENT_COUNT = 5

env = Environment(
    loader=FileSystemLoader(TEMPLATES_DIR),
    autoescape=select_autoescape()
)

# Start with an empty docs folder
if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir()

posts = []
for path in POSTS_DIR.glob("*.md"):
    post = frontmatter.load(path, encoding="utf-8")
    html = markdown.markdown(post.content, extensions=["fenced_code", "tables", "codehilite"], extension_configs={
        "codehilite": {"guess_lang": False},
    },)
    template = env.get_template(post.get("template", DEFAULT_TEMPLATE))
    page = template.render(title=post["title"], date=post["date"], content=html)
    slug = path.stem
    out_file = OUTPUT_DIR / "posts" / slug / "index.html"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(page, encoding="utf-8")
    posts.append({"title": post["title"], "date": post["date"], "url":f"/posts/{slug}/"})

posts.sort(key=lambda p: p["date"], reverse=True)

projects = []
for path in PROJECTS_DIR.glob("*.md"):
    proj = frontmatter.load(path, encoding="utf-8")
    html = markdown.markdown(proj.content, extensions=["fenced_code", "tables", "codehilite"], extension_configs={
        "codehilite": {"guess_lang": False},
    },)
    template = env.get_template(proj.get("template", DEFAULT_TEMPLATE))
    page = template.render(title=proj["title"], date=proj["date"], summary=proj.get("summary",""), content=html)
    slug = path.stem
    out_file = OUTPUT_DIR / "projects" / slug / "index.html"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(page, encoding="utf-8")
    projects.append({"title": proj["title"], "date": proj["date"], "summary": proj.get("summary",""), "url":f"/projects/{slug}/"})

projects.sort(key=lambda p: p["date"], reverse=True)

photo_files = [p for p in PHOTOS_DIR.rglob("*") if p.suffix.lower() in IMAGE_TYPES]
photos = sorted("/" + p.relative_to(STATIC_DIR).as_posix() for p in photo_files)

index = env.get_template("index.html").render(
    posts=posts[:RECENT_COUNT], 
    projects=projects,
    photos=photos
)
(OUTPUT_DIR / "index.html").write_text(index, encoding="utf-8")

if STATIC_DIR.exists():
    shutil.copytree(STATIC_DIR, OUTPUT_DIR, dirs_exist_ok=True)

print(f"built")
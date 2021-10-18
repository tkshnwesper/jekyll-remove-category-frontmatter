import sys
from pathlib import Path
import frontmatter

def delete_metadata_attribute(post, attribute):
    if attribute in post.metadata:
      del post.metadata[attribute]

if __name__ == '__main__':
  root = Path(sys.argv[1])
  if not root.is_dir():
    raise RuntimeError(f'{root.absolute()} needs to be a directory')
  
  for file in root.glob('**/_posts/*.m*d*'):
    post = frontmatter.load(file)
    delete_metadata_attribute(post, 'category')
    delete_metadata_attribute(post, 'categories')
    frontmatter.dump(post, file)

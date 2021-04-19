from simpleicons.icon import Icon

class _Icons(dict):
  def get(self, target_name: str):
    if target_name in self:
      return icons[target_name]
    
    normalized_name = target_name.lower()
    
    for key, icon in self.items():
      if icon.slug == normalized_name:
        return icon
      
      if icon.title.lower() == normalized_name:
        return icon

icons = _Icons({{
{icons}
}})

def namedivider(full_name):
  """
  Separates a full name into first and last name.

  Args:
      full_name: A string containing the full name.

  Returns:
      A tuple containing the first name and last name (or None for last name if only first name provided).
  """
  parts = full_name.split()
  if len(parts) == 1:
    return parts[0], None
  else:
    return parts[0], " ".join(parts[1:])

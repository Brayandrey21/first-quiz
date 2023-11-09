def test_alchemy_combine():

  assert alchemy_combine(
    make_oven(),
    ["lead", "mercury"],
    1064°C
  ) == "gold"

  assert alchemy_combine(
    make_oven(),
    ["water", "air"],
    -2°
  ) == "snow"

  assert alchemy_combine(
    make_oven(),
    ["cheese", "dough", "tomato"],
    220°
  ) == "pizza"

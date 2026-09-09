# celebe

Ratings and analytics for public VK pages: subscriber dynamics and
engagement. Free, no login.

**Website: [https://celebe.ru](https://celebe.ru)**

## What's inside

- `vk_engagement.py` — engagement and growth calculator: feed it a CSV of
  your own page's post stats and it prints per-post engagement plus the
  average and subscriber growth for the period.

```bash
python vk_engagement.py posts.csv
```

CSV columns: `date,subscribers,likes,comments,reposts` (one post per line).

## Why this repo

`vk_engagement.py` is a small, dependency-free example of the kind of
analytics celebe runs as a web tool. The full product lives at
[https://celebe.ru](https://celebe.ru).

## License

MIT

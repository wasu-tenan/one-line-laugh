# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/wasu-tenan/one-line-laugh-01/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![Reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/wasu-tenan/one-line-laugh-01/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

A one-line laugh for [The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f) on make.fun: one funny sentence, at most 200 characters, on any subject — judged pairwise by the house judge on surprise at the end, an everyday truth, and economy of words.

## The line

> I bought a standing desk to fix my posture, and now I slouch vertically.

## How it works

`main.py` (Python 3, standard library only) writes the line to `/output/entry.txt`, honouring `$MAKEFUN_OUTPUT_DIR` or `--output`. It validates the entry first: 1–200 characters, not only whitespace, exactly one sentence.

```sh
python3 main.py
python3 main.py --output out/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

# Contributing to Dotes

Thanks for being here. Dotes gets better when people try it on real problems, build things with it and say plainly where it falls short.

## Ways to take part

| You want to... | Do this |
| --- | --- |
| Share something you built | Open an issue with the **I built something** template |
| Suggest a change to the canon | Open an issue with the **Canon question** template first |
| Add prompts, personas, translations or tools | Open a pull request |
| Report a mistake | Open an issue, or fix it in a pull request |
| Talk it through first | Write to Michael Robbins at [michael@intospatia.xyz](mailto:michael@intospatia.xyz) |

## Ground rules

1. **Fictional or consented data only.** Never post a real person's dotes in an issue, pull request, test file or demo, and never a young person's. Sample data must be invented, and must say so.
2. **No identifying details.** Even fictional dotes use first names or roles, never full names, schools, addresses or contact details.
3. **The person holds the meaning.** Tools may suggest; they never present a guess as the author's words. Suggestions stay labeled until the author accepts them.
4. **Keep the nine commitments** in section 10 of the canon.

## The canon

The canon in [`canon/`](canon/) is maintained by Michael Robbins. It changes deliberately, so changes start as an issue. Say what you'd change, why, and what problem it solves. Small fixes, such as typos and broken links, can go straight to a pull request.

## Adding a persona

- Make the person and everyone in their stories fictional.
- Follow the format of the existing files in [`personas/`](personas/): a short description, key people, voice, a table of the collection, then each dote in full.
- Use the canon's category and subcategory names exactly, and start each dote from one of the canon's starter prompts.
- Fill in every setting: also seen through, sensitive topic, who can see it, and whether a Rep may use it.
- Add the dotes to [`data/dotes.json`](data/dotes.json) and run `python tools/validate.py data/dotes.json`.

## Adding prompts for a new audience

The 35 intents in section 6 of the canon stay fixed. Prompts are written from them for a particular age group, language or setting. Add a file under `prompts/` named for the audience, for example `prompts/adult-learners.md` or `prompts/es.md`, with three prompts per subcategory. Follow the seven rules in "How these prompts are written" in Part 2 of the canon: start with doing, ask for one moment, make sure anyone can answer, and never ask for a confession or a report on someone else.

## Writing style

- Plain English. Define any term of art the first time you use it.
- Short sentences and short paragraphs.
- Say what something is, rather than what it is not.

## How we treat each other

Be generous with credit and specific with criticism. Argue with ideas, not people. Assume the person you're talking to cares about getting this right, because they probably do.

## License

By contributing, you agree that your contributions to content are licensed under [CC BY 4.0](LICENSE) and your contributions to code under the [MIT License](LICENSE-CODE). The name "Dotes" stays free for everyone to use; see the License section of the [README](README.md).

---

By Michael Robbins · [michael@intospatia.xyz](mailto:michael@intospatia.xyz) · [dotes.xyz](https://dotes.xyz) · Free to use and adapt under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), the name "Dotes" included.

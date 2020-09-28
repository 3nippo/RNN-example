import pickle

repos_order = []
repos_counters = {}
last_repo = ""

with open('src_encs') as encs, \
     open('src', 'w', encoding='utf-8') as src:
    counter = 0
    for line in encs:
        line = list(filter(None, line.split(' ')))

        filename = " ".join(line[:-2])

        if not filename:
            continue

        filename = filename[:-1].replace("'", "\'")

        repo_name = filename.split('/')[2]

        if repo_name != last_repo:
            repos_counters[last_repo] = counter

            counter = 0
            last_repo = repo_name
            repos_order.append(repo_name)

        encoding = line[-1].split('=')[1]

        try:
            with open(filename, 'r', encoding=encoding, errors='ignore') as single_src:
                content = single_src.read()
        except LookupError:
            continue

        counter += len(content)

        src.write(content)
        src.write('\n')

if counter:
    repos_counters[last_repo] = counter

counters = [(repo, repos_counters[repo]) for repo in repos_order]

with open('repos_counts', 'wb') as counters_file:
    pickle.dump(counters, counters_file)

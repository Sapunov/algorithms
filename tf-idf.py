"""TF-IDF - Term Frequency – Inverse Document Frequency

Numerical statistic that is intended to reflect how important a word is
to a document in a collection of documents.

All text's preparations excluded and here we operate only tokens

@link: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
"""


def create_invert_index(texts):
    """Support function to create inverted index

    Inverted index is an index data structure storing a mapping from
    content, such as words or numbers, to its locations in a database
    file, or in a document or a set of documents.

    Parameters
    ----------
    texts: list
        A list of documents tokens. Each element in texts is a list of
        tokens in a specific document. Index in texts is a document_id.

    Returns
    -------
    index: dict
        Inverted index of words. Each key is a token and each value of
        the dict is a list of tuples: (a, b), where a is a document_id
        and b is a token frequency in a specific document

    doc_counts: dict
        Keys in this dict is document_ids and values - number of words
        in a specific documents. This dict very helpfull in tf-idf
        calculations
    """

    index = {}
    doc_counts = {}

    for idx, tokens in enumerate(texts):
        for token in tokens:
            if idx in doc_counts:
                doc_counts[idx] += 1
            else:
                doc_counts[idx] = 1

            if token not in index:
                index[token] = [(idx, 1)]
            else:
                for i in range(len(index[token])):
                    if index[token][i][0] == idx:
                        index[token][i] = (idx, index[token][i][1] + 1)
                        break
                else:
                    index[token].append((idx, 1))

    return index, doc_counts


def tf_idf(token, document_id, index, doc_counts):
    """TF-IDF calculations

    Parameters
    ----------
    token: str
        Word token. It must be in index

    dicument_id: int
        Document_id which the calculations is carried out

    index: dict
        Inverted index from `create_invert_index` output

    doc_counts: dict:
        Dictionary with the number of words in every document

    Returns
    -------
    tf * idf: float
        TF-IDF coefficient
    """

    tf = 0

    if token in index:
        for doc in index[token]:
            if doc[0] == document_id:
                tf = doc[1] / doc_counts[document_id]

    idf = len(doc_counts) / len(index[token])

    return tf * idf


def search(token, index, doc_counts):
    """Example search function to show how to use function above

    Parameters
    ----------
    token: str
        Word token

    index: dict
        Inverted index from `create_invert_index` output

    doc_counts: dict:
        Dictionary with the number of words in every document

    Returns
    -------
    Results: list or None
        List with document ids sorted by relevance
    """

    results = index.get(token, None)
    results_ranged = []

    if results is not None:
        for result in results:
            doc_id = result[0]

            results_ranged.append(
                (tf_idf(token, doc_id, index, doc_counts), doc_id)
            )

        return [res[1] for res in sorted(results_ranged)]

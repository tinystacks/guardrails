import pytest
from guardrails.stores.context import ContextStore
from tests.unit_tests.mocks import MockDocumentStore

def test_context_store_is_singleton ():
    context_store_1 = ContextStore()
    context_store_2 = ContextStore()

    assert context_store_1 == context_store_2

a_doc_store = MockDocumentStore()
@pytest.mark.parametrize(
    "doc_store,expected_doc_store",
    [
        (a_doc_store, a_doc_store)
        (None, None)
    ]
)
def test_set_and_get_document_store(doc_store, expected_doc_store):
    context_store = ContextStore()

    context_store.set_document_store(doc_store)

    actual_doc_store = context_store.get_document_store()

    assert actual_doc_store == expected_doc_store

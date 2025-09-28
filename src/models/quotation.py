from .base import Base


class Quotation(Base):
    DATA_FILE = "quotations.json"

    @classmethod
    def find_by_params(cls, **attrs) -> list[dict]:
        """
        Find a list of quotations by attributes.
        Returns:
            - All quotations if no params are passed
            - Empty list if no quotation is found by passed params
        """
        quotations = cls.find_all()

        if not attrs:
            return quotations

        author_id = attrs.get("author_id")
        source_id = attrs.get("source_id")
        tag_id = attrs.get("tag_id")

        results = [
            quotation
            for quotation in quotations
            if quotation["author_id"] == author_id
            or quotation["source_id"] == source_id
            or tag_id in quotation["tag_ids"]
        ]

        return results

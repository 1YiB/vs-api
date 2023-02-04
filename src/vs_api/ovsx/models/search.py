# needs to be rewritten


from dataclasses import dataclass


@dataclass()
class search_base:

    totalSize:int
    extensions:list


class search:
    def __new__(cls,data) -> search_base:

        exts = []
        for ext in data.get("extensions"):
            exts.append({
                "name":ext.get("name"),
                "displayName":ext.get("displayName"),
                "namespace":ext.get("namespace"),
                "description":ext.get("description"),
                "version":ext.get("version"),
                "avgRating":ext.get("averageRating"),
                "downloads":ext.get("downloadCount")
            })

        return search_base(
            totalSize=data.get("totalSize"),
            extensions=exts
        )

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        # strip() all values
        context = {k: v.strip() if isinstance(v, str) else v for k, v in context.items()}
        
        # title() on author name if present
        author_name = context.get("project_author_name")
        if isinstance(author_name, str) and author_name != "":
            context["project_author_name"] = author_name.title()
        
        # project_author
        if context.get("project_author_name") and context.get("project_author_email"):
            if context.get("package_manager") == "poetry":
                context["project_author"] = f"{context['project_author_name']} <{context['project_author_email']}>"
            else:
                context["project_author"] = "{" + f' name = "{context["project_author_name"]}", email = "{context["project_author_email"]}" ' + "}"
        elif context.get("project_author_name"):
            if context.get("package_manager") == "poetry":
                context["project_author"] = context["project_author_name"]
            else:
                context["project_author"] = "{" + f' name = "{context["project_author_name"]}" ' + "}"
        elif context.get("project_author_email"):
            if context.get("package_manager") == "poetry":
                context["project_author"] = context["project_author_email"]
            else:
                context["project_author"] = "{" + f' email = "{context["project_author_email"]}" ' + "}"
        else:
            context["project_author"] = ""
        
        # add i18n as middleware if it's in features
        if "i18n" in context.get("features", []):
            if context.get("middlewares") is None:
                context["middlewares"] = []
            if "i18n" not in context["middlewares"]:
                context["middlewares"].append("i18n")
        
        return context

from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    def hook(self, context):
        # strip() all values
        context = {k: v.strip() if isinstance(v, str) else v for k, v in context.items()}
        return context

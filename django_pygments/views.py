# vim: set fileencoding=utf-8 :
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.html import escape


def demo(request):
    raw_snippet="""
class ListHtmlFormatter(HtmlFormatter):
    def wrap(self, source, outfile):
        return self._wrap_div(self._wrap_pre(self._wrap_list(source)))

    def _wrap_list(self, source):
        yield 0, '<ol>'
        for i, t in source:
            if i == 1:
                # it's a line of formatted code
                t = '<li><div class="line">%s</div></li>' % t
            yield i, t
        yield 0, '</ol>'
    # a unicode comment: âăşţîÂĂŞŢÎ èéòçàù
    """
    snippet = '<pre lang="python">' + escape(raw_snippet) + '</pre>'
    return render_to_response('django_pygments/demo.html', locals(), context_instance=RequestContext(request))

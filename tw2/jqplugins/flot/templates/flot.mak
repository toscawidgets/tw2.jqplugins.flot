<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}"
	style="width:${w.attrs['width']};height:${w.attrs['height']}"></div>
  <div id="flotLabel">${w.label}</div>
  <script type="text/javascript">
	% if w.data:
    $.plot($("#${w.selector|n}"), ${w._data|n}, ${w._options|n});
	% endif
  </script>
</div>

 

(function(tinymce) {
	tinymce.create('tinymce.plugins.ImageListPlugin', {
		init : function(ed, url) {
			// Register commands
			ed.addCommand('mceImageList', function() {
				ed.windowManager.open({
					file : url + '/imagelist.htm',
					width : 450 + parseInt(ed.getLang('imagelist.delta_width', 0)),
					height : 400 + parseInt(ed.getLang('imagelist.delta_height', 0)),
					inline : 1
				}, {
					plugin_url : url
				});
			});

			// Register buttons
			ed.addButton('imagelist', {title : 'imagelist.imagelist_desc', cmd : 'mceImageList',   'class' : 'mce_image'});
		},

		getInfo : function() {
			return {
				longname : 'ImageList',
				author : 'Julien Bouquillon',
				authorurl : 'http://revolunet.com',
				infourl : 'http://github.com/revolunet/django-chunks',
				version : tinymce.majorVersion + "." + tinymce.minorVersion
			};
		}
	});

	// Register plugin
	tinymce.PluginManager.add('imagelist', tinymce.plugins.ImageListPlugin);
})(tinymce);
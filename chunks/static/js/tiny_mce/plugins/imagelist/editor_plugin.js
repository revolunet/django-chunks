(function(a){a.create("tinymce.plugins.ImagelistPlugin",{init:function(b,c){b.addCommand("mceImagelist",function(){b.windowManager.open({file:c+"/imagelist.htm",width:400+parseInt(b.getLang("imagelist.delta_width",0)),height:400+parseInt(b.getLang("imagelist.delta_height",0)),inline:1},{plugin_url:c})});b.addButton("imagelist",{title:"imagelist.imagelist_desc",cmd:"mceImagelist","class":"mce_image"})},getInfo:function(){return{longname:"ImageList Plugin",author:"revolunet",authorurl:"http://revolunet.com",infourl:"http://github.com/revolunet",version:a.majorVersion+"."+a.minorVersion}}});a.PluginManager.add("imagelist",a.plugins.ImagelistPlugin)})(tinymce);
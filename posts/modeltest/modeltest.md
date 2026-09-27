---
title: modeltest
date: 2026-09-27
template: post.html
summary: blank
visible: "true"
---
Look at my 3d model!
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>

<div style="display:flex; flex-direction:row; align-items:center; justify-content:center;">
	<model-viewer src=".glb" ar ar-modes="webxr scene-viewer quick-look" camera-controls tone-mapping="neutral" poster="poster.webp" shadow-intensity="1" exposure="0.17" environment-image="legacy" auto-rotate style="width:100%; height:1000px;"> </model-viewer>
</div>

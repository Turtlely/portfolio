---
title: modeltest
date: 2026-09-27
template: post.html
summary: blank
visible: "false"
---
# Ta da!
Look at my 3d model!
<script type="module" src="https://cdn.jsdelivr.net/npm/@google/model-viewer/dist/model-viewer.min.js"></script>

<div style="display:flex; flex-direction:row; align-items:center; justify-content:center;">
	<model-viewer src=".glb" ar ar-modes="webxr scene-viewer quick-look" camera-controls tone-mapping="neutral" poster="poster.webp" shadow-intensity="1" exposure="0.17" environment-image="legacy" auto-rotate style="width:100%; height:1000px; background-color: #F0EAD6;"> </model-viewer>
</div>

I can now display models in the post webpages!

This is done via the model-viewer tag that google has created and open sourced.

I'm thinking of integrating some of these 3D views into the project writeup pages so you can take a close look at the PCBs, enclosures etc. should make things feel more interactive.

This page will come down soon but for now you can just play around with this model
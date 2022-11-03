bl_info = {
	"name": "Koikatsu to PES",
	"category": "Rigging",
	"author": "MFG",
	"version": "0.0.2"
}

import bpy, fnmatch

def doTheThing(context, booby_physics=False):
	obj = context.active_object

	rename = {
		"cf_s_shoulder02_L": "sk_shoulder_l",
		"cf_s_arm01_L": "dsk_upperarm_l",
		"cf_s_arm03_L": "sk_upperarm_l",
		"cf_s_forearm02_L": "sk_forearm_l",
		"cf_s_wrist_L": "dsk_forearm_l",
		"cf_s_elbo_L": "dsk_elbow_l",
		"cf_s_shoulder02_R": "sk_shoulder_r",
		"cf_s_arm01_R": "dsk_upperarm_r",
		"cf_s_arm03_R": "sk_upperarm_r",
		"cf_s_forearm02_R": "sk_forearm_r",
		"cf_s_wrist_R": "dsk_forearm_r",
		"cf_s_elbo_R": "dsk_elbow_r",
		"cf_s_spine03": "sk_chest",
		"cf_s_spine01": "sk_belly",
		"cf_s_waist01": "dsk_hip",
		"cf_s_thigh01_L": "sk_thigh_l",
		"cf_d_kneeF_L": "dsk_knee_l",
		"cf_s_leg02_L": "sk_leg_l",
		"Left ankle": "sk_foot_l",
		"Left toe": "dsk_toe_l",
		"cf_s_thigh01_R": "sk_thigh_r",
		"cf_d_kneeF_R": "dsk_knee_r",
		"cf_s_leg02_R": "sk_leg_r",
		"Right ankle": "sk_foot_r",
		"Right toe": "dsk_toe_r",
		"cf_s_head": "sk_head",
		"cf_s_neck": "sk_neck",
		"cf_s_bust01_L": "breast_l",
		"cf_s_bust01_R": "breast_r",
		"cf_d_hand_R": "dsk_wrist_r",
		"cf_s_hand_R": "sk_hand_r",
		"Thumb0_R": "skh_thumb_mata_r",
		"Thumb1_R": "skh_thumb_mcp_r",
		"Thumb2_R": "skh_thumb_pip_r",
		"IndexFinger1_R": "skh_index_mcp_r",
		"IndexFinger2_R": "skh_index_pip_r",
		"IndexFinger3_R": "skh_index_dip_r",
		"MiddleFinger1_R": "skh_middle_mcp_r",
		"MiddleFinger2_R": "skh_middle_pip_r",
		"MiddleFinger3_R": "skh_middle_dip_r",
		"RingFinger1_R": "skh_ring_mcp_r",
		"RingFinger2_R": "skh_ring_pip_r",
		"RingFinger3_R": "skh_ring_dip_r",
		"LittleFinger1_R": "skh_pinky_mcp_r",
		"LittleFinger2_R": "skh_pinky_pip_r",
		"LittleFinger3_R": "skh_pinky_dip_r",
		"cf_d_hand_L": "dsk_wrist_l",
		"cf_s_hand_L": "sk_hand_l",
		"Thumb0_L": "skh_thumb_mata_l",
		"Thumb1_L": "skh_thumb_mcp_l",
		"Thumb2_L": "skh_thumb_pip_l",
		"IndexFinger1_L": "skh_index_mcp_l",
		"IndexFinger2_L": "skh_index_pip_l",
		"IndexFinger3_L": "skh_index_dip_l",
		"MiddleFinger1_L": "skh_middle_mcp_l",
		"MiddleFinger2_L": "skh_middle_pip_l",
		"MiddleFinger3_L": "skh_middle_dip_l",
		"RingFinger1_L": "skh_ring_mcp_l",
		"RingFinger2_L": "skh_ring_pip_l",
		"RingFinger3_L": "skh_ring_dip_l",
		"LittleFinger1_L": "skh_pinky_mcp_l",
		"LittleFinger2_L": "skh_pinky_pip_l",
		"LittleFinger3_L": "skh_pinky_dip_l"
	}

	mix_to = {}

	for i in obj.vertex_groups:
		if i.name in rename:
			i.name = rename[i.name]
			mix_to[i.name] = i
		elif i.name in rename.values():
			mix_to[i.name] = i

	mix = {
		"cf_s_arm02_L": "dsk_upperarm_l",
		"cf_s_forearm01_L": "sk_forearm_l",
		"cf_s_elboback_L": "dsk_elbow_l",
		"cf_s_arm02_R": "dsk_upperarm_r",
		"cf_s_forearm01_R": "sk_forearm_r",
		"cf_s_elboback_R": "dsk_elbow_r",
		"cf_s_spine02": "sk_chest",
		"cf_s_siri_L": "dsk_hip",
		"cf_s_siri_R": "dsk_hip",
		"cf_s_ana": "dsk_hip",
		"cf_j_ana": "dsk_hip",
		"cf_j_kokan": "dsk_hip",
		"cf_s_thigh02_L": "sk_thigh_l",
		"cf_s_thigh03_L": "sk_thigh_l",
		"cf_s_leg03_L": "sk_leg_l",
		"cf_s_leg01_L": "sk_leg_l",
		"cf_s_kneeB_L": "dsk_knee_l",
		"cf_s_thigh02_R": "sk_thigh_r",
		"cf_s_thigh03_R": "sk_thigh_r",
		"cf_s_leg03_R": "sk_leg_r",
		"cf_s_leg01_R": "sk_leg_r",
		"cf_s_kneeB_R": "dsk_knee_r",
		"cf_s_waist02": "dsk_hip",
		"cf_s_head": "sk_head",
		"cf_s_neck": "sk_neck",
	}

	wildcard_mix = {
		"cf_J_Vagina_*": "dsk_hip",
		"*bnip*_R": "breast_r",
		"*bnip*_L": "breast_l",
		"*bust*_R": "breast_r",
		"*bust*_L": "breast_l",
		"cf_j_toes*_R": "dsk_toe_r",
		"cf_j_toes*_L": "dsk_toe_l",
		"Left Eye": "sk_head",
		"Right Eye": "sk_head",
		"cf_J_Cheek*": "sk_head",
		"cf_J_Chin*": "sk_head",
		"cf_J_Ear*": "sk_head",
		"cf_J_Eye*": "sk_head",
		"cf_J_Face*": "sk_head",
		"cf_J_Mayu*": "sk_head",
		"cf_J_Mouth*": "sk_head",
		"cf_J_Nose*": "sk_head"
	}

	delete_list = [
		"cf_s_leg_L",
		"cf_s_leg_R"
	]

	def delete_and_normalize(vg):
		print('Removing '+vg.name)
		obj.vertex_groups.remove(vg)
		bpy.ops.object.vertex_group_normalize_all()

	def weight_mix(a, b, weight=1.0, delete=True):
		print('Mixing '+b.name+' to '+a.name)
		mod = obj.modifiers.new('Vertex Weight Mix', 'VERTEX_WEIGHT_MIX')
		mod.vertex_group_a = a.name
		mod.vertex_group_b = b.name
		mod.mix_mode = 'ADD'
		mod.mix_set = 'ALL'
		mod.mask_constant = weight
		bpy.ops.object.modifier_apply(modifier=mod.name)
		if delete: delete_and_normalize(b)

	def get_in_mix(vg):
		if vg.name in mix: return mix_to[mix[vg.name]]
		return None

	def wildcard_match(vg):
		for pattern, to in wildcard_mix.items():
			if fnmatch.fnmatch(vg.name, pattern):
				return mix_to[wildcard_mix[pattern]]
		return None

	for i in obj.vertex_groups:
		if not i.name in rename.values():
			to = get_in_mix(i)
			if to is None:
				to = wildcard_match(i)
			if to is not None:
				weight_mix(to, i)
			elif i.name in delete_list:
				delete_and_normalize(i)

	if 'breast_l' in mix_to:
		if booby_physics:
			weight_mix(mix_to['sk_chest'], mix_to['breast_l'], weight=0.9, delete=False)
			weight_mix(mix_to['sk_thigh_l'], mix_to['breast_l'], weight=0.1)
			weight_mix(mix_to['sk_chest'], mix_to['breast_r'], weight=0.9, delete=False)
			weight_mix(mix_to['sk_thigh_r'], mix_to['breast_r'], weight=0.1)
		else:
			weight_mix(mix_to['sk_chest'], mix_to['breast_l'])
			weight_mix(mix_to['sk_chest'], mix_to['breast_r'])

	bpy.ops.object.vertex_group_remove_unused()

class KoikatsuToPES(bpy.types.Operator):
	"""Convert vertex groups from Koikatsu to PES"""
	bl_idname = "object.kk_to_pes"
	bl_label = "PESify Koikatsu vertex groups"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		doTheThing(context)

		return {'FINISHED'}

class KoikatsuToPESformaDeHorny(bpy.types.Operator):
	"""Convert vertex groups from Koikatsu to PES (w/ booby physics)"""
	bl_idname = "object.kk_to_pes_boobies"
	bl_label = "PESify Koikatsu vertex groups (w/ Booby Jiggles)"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		doTheThing(context, booby_physics=True)

		return {'FINISHED'}

def register():
	bpy.utils.register_class(KoikatsuToPES)
	bpy.utils.register_class(KoikatsuToPESformaDeHorny)

def unregister():
	bpy.utils.unregister_class(KoikatsuToPES)
	bpy.utils.unregister_class(KoikatsuToPESformaDeHorny)

if __name__ == "__main__":
	register()


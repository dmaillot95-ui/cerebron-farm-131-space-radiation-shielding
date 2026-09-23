import json,hashlib,pathlib,platform
import math
mu=.12;areal=20.;dose0=1.;dose=dose0*math.exp(-mu*areal);out={"mu_cm2_g":mu,"areal_density_g_cm2":areal,"relative_dose":dose,"attenuation":1-dose};ok=0<dose<dose0
out.update({"farm":131,"engine":"python-engineering-batch-canary","engine_version":platform.python_version(),"test":"SHIELD_ATTENUATION","status":"REAL_ENGINE_CANARY_OK" if ok else "FAIL","epistemic_status":"ENGINEERING_CANARY_NOT_PHYSICAL_VALIDATION"});raw=json.dumps(out,sort_keys=True).encode();out["result_sha256"]=hashlib.sha256(raw).hexdigest();pathlib.Path("artifacts").mkdir(exist_ok=True);pathlib.Path("artifacts/f131_engine_canary.json").write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out));raise SystemExit(0 if ok else 1)
